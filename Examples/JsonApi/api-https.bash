#!/bin/bash
envIp=${1}
TOKEN=$( curl -v -c cookies.txt -b cookies.txt https://"${envIp}"/json/getToken/ )

INPUT=$(cat ${2})

COMMAND="curl -v  \
-c cookies.txt \
-b cookies.txt \
--header \"X-CSRFToken: \"${TOKEN} \
--header \"Content-Type: application/json\" \
-d '$(cat ${2})' \
https://${envIp}/json/"

eval ${COMMAND} > ${2}.Response.json

