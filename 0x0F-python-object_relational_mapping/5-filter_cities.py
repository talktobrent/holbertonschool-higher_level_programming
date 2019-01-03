#!/usr/bin/python3

""" lists all cities from given state """


from sys import argv
import MySQLdb

if __name__ == "__main__":

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    cursor = database.cursor()
    cursor.execute("""SELECT name
                      FROM cities
                      WHERE state_id = (SELECT id FROM states
                      WHERE name=%s)
                      ORDER BY cities.id""", (argv[4],))
    rows = cursor.fetchall()
    mylist = []
    for x in rows:
        mylist.append(x[0])
    print(", ".join(mylist))
    cursor.close()
    database.close()
