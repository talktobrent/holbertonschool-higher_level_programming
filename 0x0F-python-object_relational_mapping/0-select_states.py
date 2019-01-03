#!/usr/bin/python3

""" lists all states from given database """


from sys import argv
import MySQLdb

if __name__ == "__main__":

    database = MySQLdb.connect(host="localhost",
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for x in rows:
        print (x)
