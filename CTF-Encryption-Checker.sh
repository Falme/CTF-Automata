#!/usr/bin/env bash

if [[ -z  "$1" ]]; then
        echo "Not Valid argument"
        echo "Example: CTF-Encryption-Checker-sh Encr1pt3dD4t4 flag{"
        exit 0
fi

flagKey="flag{"

if [[ ! -z "$2" ]]; then
        flagKey="$2"
fi

# Tring to find a flag using ROT13

echo "== ROT13 =="
echo ""
output=$(echo "$1" | tr 'N-ZA-Mn-za-m' 'A-Za-z')
echo "${output}"

output=$(echo "$output" | tr 'N-ZA-Mn-za-m' 'A-Za-z')
echo "${output}"
