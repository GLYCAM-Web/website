#!/bin/bash

usage() {
    cat << USAGE >&2


Usage:

    bash mac-api-http.sh [JSON_INPUT] [HOST]

Designed to work on Mac dev env. Port forwarding across Docker Desktop's VM is involved.

~ JSON_INPUT is required. It should be the path to your json request file.

~ HOST is optional. If no host is provided the local dev env will be tested.


NOTE: For now, if a test requires an upload file, use file_api-http.sh Currently in dev.

Example:

   bash api-http.sh cb/evaluate_sequence.json glycam.org


USAGE
    exit 1
}

if [ "$1" == "" ]; then
    usage
fi

if [ "$2" == "" ]; then
    ##envIp=$( cat ../../../../../Proxy/env.txt )
    protocol="http://localhost:8000"
else
    envIp=${2}
    protocol="https://"
fi

INPUT=$(cat ${1})
echo "Testing: ${1}"
echo "Testing target host: ${envIp}"

TOKEN=$( curl -v -c cookies.txt -b cookies.txt "${protocol}${envIp}"/json/getToken/ )

COMMAND="curl -v  \
-c cookies.txt \
-b cookies.txt \
--header \"X-CSRFToken: \"${TOKEN} \
--header \"Content-Type: application/json\" \
-d '$(cat ${1})' \
${protocol}${envIp}/json/"

echo command: ${COMMAND}
eval ${COMMAND} > ${1}.git-ignore-me_response.json
cat ${1}.git-ignore-me_response.json
