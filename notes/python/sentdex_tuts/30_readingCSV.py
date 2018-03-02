# Reading data from CSV files

'''
' CSV files are a popular file type for data analysis and are very commonly
' used for importing/exporting data.
' CSV stands for Comma Seperated Variables
' Even though it says comma, we can use/have any form of a delimiter,
' which can be anything
' CSV data is read-in as a string and needs to be converted to proper format
' before performing mathematical operations
'''

# Python has a built-in module
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

    whatColor = input("What color do you wish to know the date of? ")
    coldex = colors.index(whatColor.lower())

    theDate = dates[coldex]

    print("The date of", whatColor, "is", theDate)
