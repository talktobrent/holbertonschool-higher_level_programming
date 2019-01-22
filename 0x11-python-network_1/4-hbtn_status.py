#!/usr/bin/python3
""" fetch a website """

import requests

page = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: {}\n\t- content: {}".format(type(page.text), page.text))
