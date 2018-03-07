# SQLite intro, creating DB and table; inserting data

'''
' Its part of the standard python library
' SQLite is essentially a lite version of SQL databases, it comes with the
' power of SQL but doesn't require you to setup a db server, user etc.
' The whole DB is a single flat file.
'''
import sqlite3

# Define a connection, if the db doesn't exists its created
conn = sqlite3.connect("tutorial.db")

# Define a cursor
c = conn.cursor()

def create_table():
    # Creates the table
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(" +
              "unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    # Inserting data
    c.execute("INSERT INTO stuffToPlot VALUES(" +
              "1452549219,'2016-01-02 13:53:39','Python',8)")

    # After any modification run commit()
    conn.commit()

    c.close()
    conn.close()

create_table()
data_entry()
