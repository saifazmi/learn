# Writing to a File

'''
' There is a difference between "writing" to a file and "appending" to a file
' Writing means we overwrite anything that was already in the file.
' Appending allows us to append data to the end of the file.
'''

# Writing
text = "Sample Text to Save\nNew line!"

'''
' Using open() to define the file variable/object?
' If the file doesn't exists already it will be created
' The 'w' parameter specifies that we are going to write to the file.
' other options are 'r' (read) or 'a' (append)
' As soon as this function is called with 'w' the file is opened and CLEARED
'''
saveFile = open("exampleFile.txt", 'w') #open the file
saveFile.write(text) # write data to file
saveFile.close() # close the file
