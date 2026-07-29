#!/usr/bin/python3
"""Fetches a URL and prints the X-Request-Id response header."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
