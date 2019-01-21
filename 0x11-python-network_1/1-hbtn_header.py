#!/usr/bin/python3
""" fetch a website header """

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as page:
        print(page.info().get('X-Request-Id'))
