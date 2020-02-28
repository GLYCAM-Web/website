#!/bin/bash
envIp=${1}
TOKEN=$( curl -v -c cookies.txt -b cookies.txt http://"${envIp}"/json/getToken/ )

echo " Token is >>>

${TOKEN}

<<<
"

INPUT=$(cat ${2})

echo " Input is >>>

${INPUT}

<<<"


COMMAND="curl -v  \
-c cookies.txt \
-b cookies.txt \
--header \"X-CSRFToken: \"${TOKEN} \
--header \"Content-Type: application/json\" \
-d '$(cat ${2})' \
http://${envIp}/json/"

echo "The command is >>>

=====================================================
${COMMAND}
=====================================================

<<<"

eval ${COMMAND} > ${2}.Response.json

