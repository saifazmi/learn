# List comprehension and generator expressions

'''
' One of the most common generator is range()
' This doesn't generate a list of the given size but rather creates a
' stream of that size without commiting it to memory. But this makes it
' slower compared to list comprehension
'''

'''
' List comprehension on the other hand stores the list to the memory, but
' is faster than a generator
'''

## List comprehension, notice the []
xyz = [i for i in range(5)]
print(xyz)

# The code above produces the same output as the following code
xyz = []
for i in range(5):
    xyz.append(i)
print(xyz[:3])

## Generator expression, notice the ()
xyz = (i for i in range(5))
print(xyz) # <generator object <genexpr> at 0x7f4d55fe4d58>
# print(list(xyz)[:3]) # converting to a list

# the object can be used for iteration
for i in xyz:
    print(i)
