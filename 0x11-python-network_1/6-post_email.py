#!/usr/bin/python3
""" fetch a website and POST email"""

import requests
from sys import argv

if __name__ == "__main__":

    page = requests.post(argv[1], data={'email': argv[2]})
    print(page.text)
