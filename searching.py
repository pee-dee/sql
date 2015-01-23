__author__ = 'phil'

import _sqlite3

with _sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # use a for loop to iterate through the database, printing the results line by line
    # for row in c.execute("SELECT firstname, lastname from employees"):
        # print row
    """ The above is commented out as it only retrieves unicode. The below gives us just the values """

    c.execute("SELECT firstname, lastname from employees")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1]