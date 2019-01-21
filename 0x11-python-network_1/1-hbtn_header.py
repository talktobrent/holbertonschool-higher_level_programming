#!/usr/bin/python3
""" fetch a website header """

import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as page:
    print(page.info().get('X-Request-Id'))
