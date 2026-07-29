#!/usr/bin/python3
"""Module that fetches a URL and prints the X-Request-Id response header."""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.getheader("X-Request-Id"))
