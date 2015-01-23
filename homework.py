__author__ = 'phil'

import _sqlite3

with _sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    newcars = [
        ("Honda", "Accord", 15),
        ("Toyota", "Camry", 12),
        ("Chevrolet", "Lumina", 2),
        ("Nissan", "Altima", 9),
        ("Ford", "Fusion", 6)
    ]

    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", newcars)

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]

    c.execute("UPDATE inventory SET quantity = 16 WHERE make='Honda'")
    c.execute("UPDATE inventory SET quantity = 4 WHERE make='Chevrolet'")

    c.execute("SELECT * FROM inventory where make='Ford'")
    fords = c.fetchall()

    for f in fords:
        print "\n", f[0], f[1], f[2]