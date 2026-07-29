#!/usr/bin/python3
"""Displays the id of a GitHub user using Basic Authentication."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get("id"))
