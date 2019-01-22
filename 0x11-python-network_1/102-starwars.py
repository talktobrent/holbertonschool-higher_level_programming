#!/usr/bin/python3
""" get starwars characters """

import requests
from sys import argv

if __name__ == "__main__":

    page = requests.get('https://swapi.co/api/people/?search={}'.
                        format(argv[1]))
    names = []
    try:
        while True:
            names.extend(page.json().pop('results'))
            if page.json().get('next'):
                page = requests.get(page.json().pop('next'))
            else:
                break
        print("Number of results: {}".format(len(names)))
        for char in names:
            print(char.pop('name'))
            for film in char.pop('films'):
                page = requests.get(film)
                print("\t{}".format(page.json().pop('title')))
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("No result")
