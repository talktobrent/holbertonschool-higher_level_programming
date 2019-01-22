#!/usr/bin/python3
""" fetch a website and print a user id and name, or error """

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) < 2:
        val = ""
    else:
        val = argv[1]

    page = requests.post('http://0.0.0.0:5000/search_user', {'q': val})
    try:
        print("[{}] {}".format(page.json().pop('id'), page.json().pop('name')))
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("No result")
