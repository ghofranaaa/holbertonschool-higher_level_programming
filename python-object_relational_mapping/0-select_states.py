#!/usr/bin/python3
import MySQLdb
import sys
# Import MySQLdb module to interact with MySQL database
# Import sys module to handle command-line arguments


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user=username,
                     password=passwrd, db=database_name)

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
db.close()
