#!/usr/bin/python3
""" login and get user's github id """

import requests
from sys import argv

if __name__ == "__main__":

    page = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        print(page.json().pop('id'))
    except:
        print("None")
