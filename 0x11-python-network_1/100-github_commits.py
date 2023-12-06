#!/usr/bin/python3
"""takes  GitHub credentials"""
import requests
from sys import argv


if __name__ == "__main__":
    auth = (argv[1], argv[2])
    re = requests.get("https://api.github.com/user", auth=auth)
    print(re.json().get("id"))
