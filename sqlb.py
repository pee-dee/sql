__author__ = 'phil'

# Create a SQLite3 database and table

# import the SQLite3 library
import sqlite3

# create a new db if the db doesn't already exist
conn = sqlite3.connect("new.db")


# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

# commit the changes to the db
conn.commit()

# close the db connection
conn.close()