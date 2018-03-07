# Appending to a file

appendMe = "\nNew bit of information"

appendFile = open("exampleFile.txt", 'a')
appendFile.write(appendMe)
appendFile.close()
