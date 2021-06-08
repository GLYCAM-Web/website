#!/bin/bash

usage() {
    cat << USAGE >&2


Usage:

    bash checkStatus.sh <pUUID> <conformerID>

~ Find pUUID and conformerID in responses to build requests.

Examples:

   bash checkStatus.sh a2f6ddfc-07c3-4dc8-8ce0-fe8c0635b652 6h-g_otg_8ogt


USAGE
    exit 1
}

if [ "$1" == "" ]; then
    usage
else
    pUUID=${1}
fi

if [ "$2" == "" ]; then
    usage
else
    conformerID=${2}
fi


echo "Checking the status of: pUUID: ${pUUID}, conformerID: ${conformerID}."
echo "Testing dev.glycam.org"

TOKEN=$( curl -v -c cookies.txt -b cookies.txt https://dev.glycam.org/json/getToken/ )

COMMAND="curl -v  \
-c cookies.txt \
-b cookies.txt \
--header \"X-CSRFToken: \"${TOKEN} \
--header \"Content-Type: application/json\" \
'https://dev.glycam.org/cb/build_status/${pUUID}/${conformerID}/'"

echo ${COMMAND}
eval ${COMMAND} > status.${pUUID}.${conformerID}.git-ignore-me_response.json
cat status.${pUUID}.${conformerID}.git-ignore-me_response.json
