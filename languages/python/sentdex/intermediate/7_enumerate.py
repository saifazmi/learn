# Enumerate

'''
' Enumerate takes an iterable as parameter and returns a tuple containing
' the count of item and the item itself
' by default the count starts from index 0 but we can define start=num as param
' to change the starting point of count
'''

example = ["left", "right", "up", "down"]

# NOT the right way of doing this
for i in range(len(example)):
    print(i, example[i])

print(5*'#')

# Right way of writing the above code
for i, j in enumerate(example):
    print(i, j)

print(5*'#')

# Creating a dictionary using enumerate, where key is the index value
new_dict = dict(enumerate(example))
print(new_dict)

[print(i, j) for i, j in enumerate(new_dict)]

print(5*'#')

# Creating a list using enumerate
new_list = list(enumerate(example))
print(new_list)

[print(i, j) for i, j in enumerate(new_list, start=1)]
