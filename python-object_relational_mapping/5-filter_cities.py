#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of a specific state, using the database hbtn_0e_4_usa.
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
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    mycursor.execute(query, (state_name,))
    rows = mycursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    mycursor.close()
    db.close()
