# FOR loop

'''
' For loop is typically used to "iterate" through something
'''

# Iterating through a list
exampleList = [1,2,6,8,10,45,12,17,2,3,9]

for eachNumber in exampleList:
    print(eachNumber)

'''
' Indentation matters and defines the block of code
'''
print('continue program')

# Example of using range()
'''
' range() is a built-in function so no need for any imports
' the range() function from python3 has been backported to 2.7 as xrange()
' py2 range() will actually create a list out of the given range parameters
' which can have massive performance impact, potentially maxing out RAM
' example py2: range(1,10000000000) is a massive list, replace with xrange()
' the py3 range() and py2 xrange() is actually a generator.
'''
for x in range(1,11):
    print(x) # will print from 1 to 10
