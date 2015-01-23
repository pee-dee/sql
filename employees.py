__author__ = 'phil'

import os
import csv
import sqlite3

myPath = "/Users/phil/PycharmProjects/real_python_2/book2-exercises-master/"

myFile = os.path.join(myPath, "sql/employees.csv")

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # open the csv file and assign it to a variable
    employees = csv.reader(open(myFile, "rU"))

    # create a new table called employee
    try:
        c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
    except sqlite3.Error:
        print "table already there yo"

    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)