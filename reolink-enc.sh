#!/bin/sh
# Set video encoding (h264/h265) on Reolink cameras via HTTP API

usage() {
	echo "usage: ${0##*/} -u user -p pass -h host [-s stream] codec" >&2
	echo "  -u user    login username" >&2
	echo "  -p pass    login password" >&2
	echo "  -h host    camera IP or hostname" >&2
	echo "  -s stream  main or sub (default: main)" >&2
	echo "  codec      h264 or h265" >&2
	exit 1
}

stream="main"
while getopts "u:p:h:s:" opt; do
	case $opt in
	u) user=$OPTARG ;;
	p) pass=$OPTARG ;;
	h) host=$OPTARG ;;
	s) stream=$OPTARG ;;
	*) usage ;;
	esac
done
shift $((OPTIND - 1))
codec=$1

[ -z "$user" ] && usage
[ -z "$pass" ] && usage
[ -z "$host" ] && usage
[ -z "$codec" ] && usage

case $codec in
h264|h265) ;;
*) echo "error: codec must be h264 or h265" >&2; exit 1 ;;
esac

case $stream in
main|sub) ;;
*) echo "error: stream must be main or sub" >&2; exit 1 ;;
esac

if [ "$stream" = "main" ]; then
	skey="mainStream"
else
	skey="subStream"
fi

api="http://${host}/api.cgi"

# login
resp=$(curl -s -X POST "${api}?cmd=Login" \
	-d "[{\"cmd\":\"Login\",\"action\":0,\"param\":{\"User\":{\"userName\":\"${user}\",\"password\":\"${pass}\"}}}]")

token=$(echo "$resp" | sed -n 's/.*"name" *: *"\([^"]*\)".*/\1/p' | head -1)
if [ -z "$token" ]; then
	echo "error: login failed" >&2
	echo "$resp" >&2
	exit 1
fi

# get current encoding
cur=$(curl -s -X POST "${api}?cmd=GetEnc&token=${token}" \
	-d "[{\"cmd\":\"GetEnc\",\"action\":0,\"param\":{\"channel\":0}}]")

cur_vtype=$(echo "$cur" | sed -n 's/.*"'${skey}'".*"vType" *: *"\([^"]*\)".*/\1/p')
if [ -n "$cur_vtype" ]; then
	echo "current ${stream}Stream vType: ${cur_vtype}"
fi

if [ "$cur_vtype" = "$codec" ]; then
	echo "already set to ${codec}, nothing to do"
	# logout
	curl -s -X POST "${api}?cmd=Logout&token=${token}" \
		-d "[{\"cmd\":\"Logout\",\"action\":0,\"param\":{}}]" >/dev/null
	exit 0
fi

# set encoding
resp=$(curl -s -X POST "${api}?cmd=SetEnc&token=${token}" \
	-d "[{\"cmd\":\"SetEnc\",\"action\":0,\"param\":{\"Enc\":{\"channel\":0,\"${skey}\":{\"vType\":\"${codec}\"}}}}]")

code=$(echo "$resp" | sed -n 's/.*"rspCode" *: *\([0-9]*\).*/\1/p')

if [ "$code" = "200" ]; then
	echo "set ${stream}Stream to ${codec} (camera will reboot)"
else
	echo "error: SetEnc failed" >&2
	echo "$resp" >&2
	# logout
	curl -s -X POST "${api}?cmd=Logout&token=${token}" \
		-d "[{\"cmd\":\"Logout\",\"action\":0,\"param\":{}}]" >/dev/null
	exit 1
fi

# logout
curl -s -X POST "${api}?cmd=Logout&token=${token}" \
	-d "[{\"cmd\":\"Logout\",\"action\":0,\"param\":{}}]" >/dev/null
