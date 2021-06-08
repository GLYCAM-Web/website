#!/bin/bash

usage() {
    cat << USAGE >&2


Usage:

    bash api-http.sh [JSON_INPUT] [HOST]

~ JSON_INPUT is required. It should be the path to your json request file.

~ HOST is also required. This is usually dev.glycam.org, but might also be
   glycam.org in a future release.


Examples:

   Evaluate:
   bash api-http.sh evaluate-sequence.json dev.glycam.org

   Build Default:
   bash api-http.sh build-sequence.json dev.glycam.org

   Build w/Options:
   bash api-http.sh build-sequence-with-options.json dev.glycam.org


Output:
The above commands would create output in the same dir, named like the following:

   evaluate_sequence.json.Response.json
   build-sequence.json.Response.json
   build-sequence-with-options.json.Response.json

This file also reads that output to the command line.

USAGE
    exit 1
}

if [ "$1" == "" ]; then
    usage
fi
if [ "$2" == "" ]; then
    usage
fi

INPUT=$(cat ${1})
HOST=${2}
TOKEN=$( curl -v -c cookies.txt -b cookies.txt https://"${HOST}"/json/getToken/ )

COMMAND="curl -v  \
-c cookies.txt \
-b cookies.txt \
--header \"X-CSRFToken: \"${TOKEN} \
--header \"Content-Type: application/json\" \
-d '$(cat ${1})' \
https://${HOST}/json/"

eval ${COMMAND} > ${1}.Response.json
cat ${1}.Response.json
