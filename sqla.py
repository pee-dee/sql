__author__ = 'phil'

# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new db if the db doesn't already exist
conn = sqlite3.connect("new.db")


# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
# cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

# close the db connection
conn.close()

conn2 = sqlite3.connect("cars.db")

cursor = conn2.cursor()
cursor.execute("""CREATE TABLE inventory (make TEXT, model TEXT, quantity INT)""")
conn2.close()