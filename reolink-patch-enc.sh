#!/bin/sh
# Patch Reolink firmware to enable H.264/H.265 codec switching.
#
# Changes encoder_select="0" to encoder_select="3" in dvr.xml of the
# app partition, then repacks the PAK file with updated CRC32.
#
# Requirements: pakler, ubireader, unsquashfs, mksquashfs, ubinize
#
# Usage: reolink-patch-enc.sh firmware.pak [output.pak]

set -e

usage() {
	echo "usage: ${0##*/} firmware.pak [output.pak]" >&2
	echo "  Patches encoder_select to enable H.264/H.265 switching." >&2
	echo "  Output defaults to firmware_patched.pak" >&2
	exit 1
}

die() {
	echo "error: $*" >&2
	exit 1
}

cleanup() {
	[ -n "$tmpdir" ] && rm -rf "$tmpdir"
}

# check arguments
[ -z "$1" ] && usage
input=$(realpath "$1")
[ -f "$input" ] || die "file not found: $1"

if [ -n "$2" ]; then
	output=$(realpath "$2")
else
	base=$(basename "$input" .pak)
	output="$(dirname "$input")/${base}_patched.pak"
fi

# check tools
for cmd in pakler ubireader_extract_images unsquashfs mksquashfs; do
	command -v "$cmd" >/dev/null 2>&1 || die "$cmd not found"
done
command -v ubinize >/dev/null 2>&1 || {
	[ -x /usr/sbin/ubinize ] || die "ubinize not found"
}
UBINIZE=$(command -v ubinize 2>/dev/null || echo /usr/sbin/ubinize)

trap cleanup EXIT
tmpdir=$(mktemp -d)

echo "==> Extracting PAK sections..."
pakler -e -d "$tmpdir/sections" "$input" || die "pakler extract failed"

app_bin="$tmpdir/sections/05_app.bin"
[ -f "$app_bin" ] || die "section 5 (app) not found in PAK"

echo "==> Extracting squashfs from app UBI..."
ubireader_extract_images -o "$tmpdir/ubi" "$app_bin" || die "UBI extract failed"

sqfs=$(find "$tmpdir/ubi" -name "*.ubifs" -type f | head -1)
[ -n "$sqfs" ] || die "no squashfs found in UBI"

# verify it is squashfs
file "$sqfs" | grep -qi squashfs || die "UBI volume is not squashfs"

echo "==> Extracting squashfs filesystem..."
unsquashfs -d "$tmpdir/appfs" "$sqfs" || die "unsquashfs failed"

dvr="$tmpdir/appfs/dvr.xml"
[ -f "$dvr" ] || die "dvr.xml not found in app filesystem"

# check current value
cur=$(sed -n 's/.*encoder_select="\([^"]*\)".*/\1/p' "$dvr")
echo "    encoder_select current value: ${cur:-not found}"

if [ "$cur" = "3" ]; then
	echo "    already set to 3, nothing to patch"
	exit 0
fi

if [ "$cur" != "0" ]; then
	die "unexpected encoder_select value: $cur (expected 0)"
fi

echo "==> Patching dvr.xml: encoder_select=\"0\" -> encoder_select=\"3\"..."
sed -i 's/encoder_select="0"/encoder_select="3"/' "$dvr"

# verify patch
new=$(sed -n 's/.*encoder_select="\([^"]*\)".*/\1/p' "$dvr")
[ "$new" = "3" ] || die "patch verification failed (got: $new)"

echo "==> Rebuilding squashfs (gzip, blocksize 16384)..."
mksquashfs "$tmpdir/appfs" "$tmpdir/app_new.sqfs" \
	-comp gzip -b 16384 -no-tailends \
	-all-root -force-uid 1050 -force-gid 1050 \
	-noappend -quiet || die "mksquashfs failed"

new_sqfs_size=$(stat -c '%s' "$tmpdir/app_new.sqfs")
orig_sqfs_size=$(stat -c '%s' "$sqfs")
echo "    squashfs size: $orig_sqfs_size -> $new_sqfs_size bytes"

# UBI parameters (from original image)
peb_size=131072
min_io=2048
sub_page=2048

# verify new squashfs fits
orig_ubi_size=$(stat -c '%s' "$app_bin")
max_lebs=$(( (orig_ubi_size / peb_size) - 2 ))  # subtract 2 layout PEBs
leb_size=$((peb_size - 2 * min_io))
max_data=$((max_lebs * leb_size))

if [ "$new_sqfs_size" -gt "$max_data" ]; then
	die "new squashfs ($new_sqfs_size) exceeds UBI capacity ($max_data)"
fi

echo "==> Rebuilding UBI image..."
cat > "$tmpdir/ubi.ini" << EOF
[app]
mode=ubi
vol_id=0
vol_type=dynamic
vol_name=app
vol_flags=autoresize
image=$tmpdir/app_new.sqfs
EOF

"$UBINIZE" -o "$tmpdir/app_new.ubi" \
	-p $peb_size -m $min_io -s $sub_page \
	"$tmpdir/ubi.ini" || die "ubinize failed"

new_ubi_size=$(stat -c '%s' "$tmpdir/app_new.ubi")
echo "    UBI size: $orig_ubi_size -> $new_ubi_size bytes"

if [ "$new_ubi_size" -gt "$orig_ubi_size" ]; then
	die "new UBI ($new_ubi_size) larger than original ($orig_ubi_size)"
fi

# pad to original size if smaller
if [ "$new_ubi_size" -lt "$orig_ubi_size" ]; then
	dd if=/dev/zero bs=1 count=$((orig_ubi_size - new_ubi_size)) 2>/dev/null \
		>> "$tmpdir/app_new.ubi"
fi

echo "==> Repacking PAK with updated app section..."
pakler -r -n 5 -f "$tmpdir/app_new.ubi" -o "$output" "$input" \
	|| die "pakler repack failed"

echo "==> Verifying..."
pakler -l "$output" 2>&1 | grep -q "passes CRC" || die "CRC verification failed"

echo ""
echo "Patched firmware: $output"
echo "Flash via Reolink app or client: Settings -> System -> Firmware -> Manual Update"
