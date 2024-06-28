#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
This script is safe from MySQL injections.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    mycursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    mycursor.execute(query, (state_name,))
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

    mycursor.close()
    db.close()
