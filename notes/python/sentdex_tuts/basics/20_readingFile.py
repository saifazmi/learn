# Reading from a file

# read() function reads in the whole file.
readMe = open("exampleFile.txt", 'r').read() # reads the files into variable

print(readMe)

# readlines() reads the file line by line and save it in a python list
readLine = open("exampleFile.txt", 'r').readlines()

print(readLine)
