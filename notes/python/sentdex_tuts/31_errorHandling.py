# Error handling with Try and Except

'''
' The "try" and "except" keywords work similar to an if/else statement
' "try" quite literally tries to run the block of code it has been assigned
' and if anywhere in that block of code it throws an exception (error)
' it will go to the "exception" block
'
' Always do your own checks before using try/except, as they should be used
' as a last ditch effort to stop the program coming to a screeching halt
'''

import csv

with open("example.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    dates = []
    colors = []
    
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatColor = input("What color do you wish to know the date of? ")

        if whatColor in colors:
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print("The date of", whatColor, "is", theDate)
        else:
            print("Color not found, or is not a color")
    # In python 2.7 the syntax will be:
    # except Exception, e:
    except Exception as e:
        print(e)

    print("continuing...")
