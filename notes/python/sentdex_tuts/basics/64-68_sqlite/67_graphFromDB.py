# SQLite ploting from DB values

import sqlite3
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()

def graph_data():
    c.execute("SELECT unix, value FROM stuffToPlot")
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-') # line style
    plt.show()

graph_data()
c.close()
conn.close()
