#!/bin/bash
# sends a GET request to the URL, following redirects, and displays the body only if final status is 200
body=$(curl -s -L -w "\n%{http_code}" "$1"); code=${body##*$'\n'}; [ "$code" = "200" ] && printf '%s' "${body%$'\n'*}"
