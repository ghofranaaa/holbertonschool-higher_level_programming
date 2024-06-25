#!/usr/bin/python3
import MySQLdb  # Import MySQLdb module to interact with MySQL database
import sys  # Import sys module to handle command-line arguments


if __name__ == "__main__":
    # Get MySQL username, password, and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

# Connect to the MySQL database
# MySQLdb.connect creates a connection object to interact with the database
db = MySQLdb.connect(host="localhost", port=3306, user=username,
                     passwd=password, db=database_name)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Execute SQL query to select all rows from the states table, ordered by id
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows returned by the SQL query
states = cursor.fetchall()

# Iterate over each row in the result set and print it
for state in states:
    print(state)

# Close the cursor to release the resources
cursor.close()

# Close the database connection
db.close()
