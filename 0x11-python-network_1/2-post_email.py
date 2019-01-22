#!/usr/bin/python3
""" POST an email address """

from urllib import parse, request
from sys import argv

if __name__ == "__main__":

    data = parse.urlencode({'email': argv[2]}).encode()

    with request.urlopen(argv[1], data) as page:
        print(page.read().decode('utf-8'))
