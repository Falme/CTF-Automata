#!/usr/bin/env bash

flagKey="$2"

strings "$1" | grep "${flagKey}"

