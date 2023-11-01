#!/usr/bin/env bash

if [[ -z  "$1" ]]; then
        echo "Not Valid argument"
        echo "Example: CTF-File-Checker-sh ~/path/to/file.txt"
        exit 0
fi

if [[ ! -e "$1" ]]; then
        echo "File Does not Exist"
        echo "Example: CTF-File-Checker-sh ~/path/to/file.txt"
        exit 0
fi

flagKey="flag{"

if [[ ! -z "$2" ]]; then
        flagKey="$2"
fi

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"


bash "$SCRIPTPATH/BasicStrings/BasicStrings.sh" "$1" "${flagKey}"

bash "$SCRIPTPATH/QRCode/QRCode.sh" "$1" "${flagKey}"
