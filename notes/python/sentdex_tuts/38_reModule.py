# Regular Expression with re in Python

'''
' Regular Expression is a programming language on its own much like SQL
' as such they remain consistent between programming languages
'
' RegEx apply to a body/string of text, it allows us to process this text
' and fetch data out of this body of text which match a certain pattern
' which is defined using RegEx
'''

'''
' Identifiers -
'
' \d : any number
' \D : anyting but a number
' \s : space
' \S : anything but a space
' \w : any character
' \W : anything but a character
' .  : any character, except a newline
' \b : the whitespace around words
' \. : a period
'
' Modifiers (description for identifiers) -
'
' {1,3} : we're expecting something of length 1 to 3 (\d{1,3})
' +     : Match 1 or more
' ?     : Match 0 or 1
' *     : Match 0 or more
' $     : match the end of a string
' ^     : match the beginning of a string
' |     : ether or (\d{1-3} | \w{5-6})
' []    : range or "variance"
' {x}   : expecting "x" amount
'
' White Space Characters - 
'
' \n : new line
' \s : space
' \t : tab
' \e : escape
' \f : form feed
' \r : return or carriage return
'
' Characters to REMEMBER TO ESCAPE IF USED!
'
' . + * ? [ ] $ ^ ( ) { } | \
'''

import re

exampleString = """
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
"""

'''
' the r"" informs python that the string is a regex
' this particular regex is looking for any number which has length of 1 to 3
'''
ages = re.findall(r"\d{1,3}", exampleString)

'''
' this regex looks for any capital letter first and then
' as many lower case letters
'''
names = re.findall(r"[A-Z][a-z]*", exampleString)

print(ages)
print(names)

# We can now create a dictionary from this data
ageDict = {}

x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1

print(ageDict)
