#!/usr/bin/python3
""" adds arguments to a JSON file """
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    ob = load_from_json_file("add_item.json")
    ob.extend(argv[1:])
    save_to_json_file(ob, "add_item.json")
except:
    save_to_json_file(argv[1:], "add_item.json")
