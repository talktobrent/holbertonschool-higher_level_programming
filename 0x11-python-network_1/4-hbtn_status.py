#!/usr/bin/python3
""" fetch a website """

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as page:
    output = page.read()
print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".
      format(type(output), output))
