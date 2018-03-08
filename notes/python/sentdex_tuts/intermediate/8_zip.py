# Zip function

'''
' Takes elements from multiple iterables and aggregates them into one
' where the index value is shared
'''

x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

##for a,b,c in zip(x,y,z):
##    print(a,b,c)

print(zip(x,y,z)) # <zip object at 0x7f406ee1fb48>

# zip object is iterable
for i in zip(x,y,z):
    print(i) # tuples of the values

# converting to a list
print(list(zip(x,y,z))) # list of tuples

# only works with two values for dict
print(dict(zip(x,z)))

# List comp
[print(a,b,c) for a,b,c in zip(x,y,z)]

print(a) # NameError: name 'a' is not defined
'''
' variables in list comp are temporary and are not stored
' but if we write a proper for loop like the one above, 'a' will be 4
'''
