#!/usr/bin/python3
""" fetch a website and print status code if an error, else print text """

import requests
from sys import argv

if __name__ == "__main__":

    page = requests.get(argv[1])
    if page.status_code >= 400:
        print("Error code: {}".format(page.status_code))
    else:
        print(page.text)
