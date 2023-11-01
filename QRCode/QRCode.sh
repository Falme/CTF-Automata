#!/usr/bin/env bash

flagKey="$2"

zbarimg -q "$1" | grep "${flagKey}"

