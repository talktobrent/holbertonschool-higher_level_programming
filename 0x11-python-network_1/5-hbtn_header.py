#!/usr/bin/python3
""" fetch a website """

import requests
from sys import argv

if __name__ == "__main__":

    page = requests.get(argv[1])
    print(page.headers['X-Request-Id'])
