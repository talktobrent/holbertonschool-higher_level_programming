#!/usr/bin/python3

""" lists all states beginning with capital N """


from sys import argv
import MySQLdb

if __name__ == "__main__":

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cursor.fetchall()
    for x in rows:
        print (x)
