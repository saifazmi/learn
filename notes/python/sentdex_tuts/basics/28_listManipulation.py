# List Manipulation

x = [2,4,5,1,6,4,1,8,9,3,4,2,3]
print(x)

# Adding/Appending value to the list
x.append(2)
print(x)

# Inserting value at a specific location
x.insert(3,99)
print(x)

# Deleting value
x.remove(2) # first occurance of value
print(x)

x.remove(x[0]) # index of the value to remove
print(x)

# Accessing value
print(x[5]) # sixth element

# Slicing
print(x[5:7]) # from index of 5 to 6 NOT 7, i.e. two values

# Last and second last element
print(x[-1])
print(x[-2])

# Index value of element
print(x.index(1))

# Count number of elements
print(x.count(99))

# Sort list (python does this intutively based on numeric or alphanetical val)
x.sort() # will change the list as it is mutable
print(x)

y = ["Janet", "Jessy", "Kelly", "Alice", "Bob", "Joe"]
y.sort()
print(y)

# Reversing a list
y.reverse()
print(y)
