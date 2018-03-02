# Python Dictionaries

'''
' One of the most useful data types in python is the python
' dictionary.
' 
' If you are familiar with other languages, think of it like an associative
' array. 
' 
' The idea of the dictionary is to have what are called keys and values.
' Despite being ordered if you print a dictionary out, there is no actual
' order to dictionaries.
'
' All keys are unique
' 
' So before we used two lists and assumed their association, searched for index,
' and found information about 1 item in 1 list from another.
'
' Now here, everything is contained in the same location, and makes more sense
'
' Let us show an example:
'''

# The curly braces define a dictionary
exDict = {"Jack":15, "Bob":22, "Alice":12, "Kevin":17}

print(exDict)

# How old is Jack?
print(exDict["Jack"])

# Adding a new key value pair
exDict["Tim"] = 14
print(exDict)

# Tim just turned 15 yo
exDict["Tim"] = 15
print(exDict)

# Tim is dead now :( gotta remove him from the dictionary
del exDict["Tim"]
print(exDict)

# Adding hair color
exDict = {
        "Jack":[15,"blonde"],
        "Bob":[22,"brown"],
        "Alice":[12,"black"],
        "Kevin":[17,"red"]
        }

print(exDict["Jack"][1])
