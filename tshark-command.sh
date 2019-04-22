INTERFACE=$1

function usage() {
	echo "usage : tshark-command.sh <interface>"
	echo "exam  : tshark-command.sh wlan0"
}

if [ -z "$INTERFACE" ]; then
	usage
	exit 1
fi

tshark -i "$INTERFACE" -T fields -e http.host -e http.request.full_uri -e urlencoded-form.value -Y "tcp contains \"11111111\""

