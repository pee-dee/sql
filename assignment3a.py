__author__ = 'phil'

import sqlite3
import random


# create db
with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # Drop table if exists and create table
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers (num INT)")

    # make for loop to add 100 randint's to db
    for i in range(100):
        # add each number into
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100),))


prompt = """Select the operation that you want to perform [1-5]:
    1. Average
    2. Max
    3. Min
    4. Sum
    5. Exit"""

# loop until user enters a valid operation number
while True:
    # get user input
    x = raw_input(prompt)

    # if user enters any choice from 1-4
    if x in {"1", "2", "3", "4"}:
        # parse the corresponding operation text
        operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[int(x)]

        # retrieve data
        c.execute("SELECT {}(num) from numbers".format(operation))

        # fetchone() retrieves one record from the query
        get = c.fetchone()

        # output result ot screen
        print operation + ": %f" % get[0]

    # if user enters 5
    elif x == "5":
        print "Exit"

        # exit loop
        break