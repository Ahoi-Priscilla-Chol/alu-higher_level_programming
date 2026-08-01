#!/bin/bash
# Sends a GET request to a given URL with a custom header, prints the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
