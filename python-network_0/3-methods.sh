#!/bin/bash
# displays all HTTP methods the server accepts for the given URL
curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | cut -d ' ' -f2-
