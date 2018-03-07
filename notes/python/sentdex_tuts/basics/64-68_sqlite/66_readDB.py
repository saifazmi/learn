# SQLite reading from DB

import sqlite3

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()

def read_from_db():
    c.execute("SELECT * FROM stuffToPlot") # this is just a selection
    data = c.fetchall() # gets the data
    print(data)
    # Generally we iterate through the data
    for row in data:
        print(row) # each row is basically a tuple


    c.execute("SELECT * FROM stuffToPlot WHERE value = 3")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute("SELECT * FROM stuffToPlot WHERE unix > 1520423573")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute("SELECT value, datestamp FROM stuffToPlot WHERE unix > 1520423573")
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

read_from_db()
c.close()
conn.close()
