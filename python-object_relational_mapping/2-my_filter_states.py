#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states \
    table of hbtn_0e_0_usa where name matches the argument.

arguments :
    mysql username: string
    mysql password: string
    database name: string
    state name searched: string
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"\
        .format(state_name_searched)
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
