# SQLite updating and deleting DB

'''
' Updating and deleting are permanent actions in DB, so make sure you really
' want to do that. For a web-server or any production db it is strongly
' recommended to have automatic backups of the DB
'''

import sqlite3

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()

# Abstracted out this function for the purpose of this tutorial
def print_db(sql):
    c.execute(sql)
    data = c.fetchall()

    # one line for loop
    [print(row) for row in data]

    return len(data)

def del_and_update():
    print_db("SELECT * FROM stuffToPlot")
##    c.execute("UPDATE stuffToPlot SET value = 99 WHERE value = 8")
##    conn.commit()
##    print_db("SELECT * FROM stuffToPlot")

##    c.execute("DELETE FROM stuffToPlot WHERE value = 99")
##    conn.commit()
##    print(60*'#')
##    print_db("SELECT * FROM stuffToPlot")

    print(60*'#')
    
    '''
    ' Since deleting is irreversible operation, it is a good practisce to check
    ' what we are going to delete or atleast the number of rows
    '''
    numRows = print_db("SELECT * FROM stuffToPlot WHERE value = 6")
    print("Number of rows:", numRows)

    
del_and_update()

c.close()
conn.close()
