__author__ = 'phil'

import _sqlite3

with _sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create a dictionary of sql queries
    sql = {
        'Focus count': "SELECT count(make) FROM orders WHERE model = 'Focus'",
        'Civic count': "SELECT count(make) FROM orders WHERE model = 'Civic'",
        'Ranger count': "SELECT count(make) FROM orders WHERE model = 'Ranger'",
        'Accord count': "SELECT count(make) FROM orders WHERE model = 'Accord'",
        'Avenber count': "SELECT count(make) FROM orders WHERE model = 'Avenger'",
    }

    # run each sql query item in the dictionary
    for keys, values in sql.iteritems():

        # run sql
        c.execute(values)

        # fetchone() retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print keys + ":", result[0]