#!/bin/bash
# sends a GET request to the URL and displays the body only if status is 200
response=$(curl -s -L -w "\n%{http_code}" "$1"); code=$(echo "$response" | tail -n1); [ "$code" = "200" ] && echo "$response" | sed '$d'
