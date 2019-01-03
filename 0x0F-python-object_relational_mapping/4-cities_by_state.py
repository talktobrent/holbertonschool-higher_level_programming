#!/usr/bin/python3

""" lists all states from given database """


from sys import argv
import MySQLdb

if __name__ == "__main__":

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    cursor = database.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                      FROM states
                      INNER JOIN cities
                      ON cities.state_id = states.id
                      ORDER BY cities.id""")
    rows = cursor.fetchall()
    for x in rows:
        print (x)
    cursor.close()
    database.close()
