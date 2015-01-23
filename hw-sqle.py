__author__ = 'phil'

import _sqlite3

with _sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    orders = [
        ('Ford', 'Focus', '2014-01-22'),
        ('Ford', 'Focus', '2014-01-23'),
        ('Ford', 'Focus', '2014-01-24'),
        ('Honda', 'Civic', '2014-01-25'),
        ('Honda', 'Civic', '2014-01-26'),
        ('Honda', 'Civic', '2014-01-27'),
        ('Ford', 'Ranger', '2014-01-28'),
        ('Ford', 'Ranger', '2014-01-22'),
        ('Ford', 'Ranger', '2014-01-23'),
        ('Honda', 'Accord', '2014-01-24'),
        ('Honda', 'Accord', '2014-01-25'),
        ('Honda', 'Accord', '2014-01-26'),
        ('Ford', 'Avenger', '2014-01-27'),
        ('Ford', 'Avenger', '2014-01-28'),
        ('Ford', 'Avenger', '2014-01-22'),
    ]

    # c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)

    c.execute("SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date FROM inventory INNER JOIN orders ON inventory.model = orders.model")

    rows = c.fetchall()

    for r in rows:
        print "Make: " + r[0] + ", Model: " + r[1]
        print "Quantity: " + str(r[2])
        print "Order Dates: " + str(r[3])
        print

