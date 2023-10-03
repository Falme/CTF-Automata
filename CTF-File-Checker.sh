#!/bin/bash

if [[ -z  "$1" ]]; then
        echo "Not Valid argument"
        echo "Example: CTF-File-Checker-sh ~/file/to/file.txt"
        exit 0
fi

if [[ ! -e "$1" ]]; then
        echo "File Does not Exist"
        echo "Example: CTF-File-Checker-sh ~/file/to/file.txt"
        exit 0
fi

flagKey="flag{"

if [[ ! -z "$2" ]]; then
        flagKey="$2"
fi


strings "$1" | grep "${flagKey}"
 
zbarimg -q "$1" | grep "${flagKey}"
