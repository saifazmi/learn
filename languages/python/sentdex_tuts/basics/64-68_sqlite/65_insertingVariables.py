# SQLite inserting data from variables into db

'''
' When it comes to real world usage, we rarely hardcode values into the db
' The values generally come from a source, stored in a variables which is
' passed into the db.
'''

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("tutorial.db")


c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(" +
              "unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def dynamic_data_entry():
    unix = time.time()

    # Converting unix time to normal date stamp
    date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    keyword = "Python"
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value)" +
              "VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))

    conn.commit()
    '''
    ' No need to close connection & cursor here as we are doing a lot
    ' of insertion and we don't want to close and open connection everytime
    '''

create_table()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1) # so the timestamp goes up a second

# Now we close cursor and connection
c.close()
conn.close()
