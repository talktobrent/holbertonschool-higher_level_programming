#!/usr/bin/python3
""" fetch a website and print status code if an error, else print text """

import requests
from sys import argv

if __name__ == "__main__":

    page = requests.get('https://swapi.co/api/people/?search={}'.
                        format(argv[1]))
    try:
        names = page.json().pop('results')
        print("Number of results: {}".format(len(names)))
        for char in names:
            print(char.pop('name'))
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("No result")
