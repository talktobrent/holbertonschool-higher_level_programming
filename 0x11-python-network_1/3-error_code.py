#!/usr/bin/python3
""" fetch a website header """

from urllib import request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":

    try:
        with request.urlopen(argv[1]) as page:
            print(page.read().decode('utf-8'))
    except HTTPError as code:
        print("Error code: {}".format(code.code))
