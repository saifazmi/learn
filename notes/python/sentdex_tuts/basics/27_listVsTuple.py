# Lists vs Tuples

'''
' A list is mutable, i.e. and provides functions to update it
' Where as a tuple is immutable and doesn't offer any update functionalities
' The main sytax difference is the () and [] brackets
'''

# Tuples
x = 5,6,2,6
y = (5,6,2,6)

# List
z = [5,6,2,6]

'''
' Most of the time we use a list but tuples have their advantages
' Squence Unpacking
' Handling a huge assortment of data we know we are not gonna change,
' as tuples are generated and iterated through faster
' when compared to a python list
'''

def exampleFunc():
    # after some work generates the numbers below
    return 15,6

a,b = exampleFunc()
print(a,b)

# Selecting data from a tuple
print(x[1])

# Selecting data from a list
print(z[0],z[3])
