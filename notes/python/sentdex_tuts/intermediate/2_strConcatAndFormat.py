# String concatenation and formatting

## Concatenation
names = ["Jeff", "Gary", "Jill", "Samantha"]

for name in names:
    print("Hello there,", name) # auto space
    print("Hello there, " + name) # much more readable, but makes another copy
    print(' '.join(["Hello there,", name])) # better for performance, no copies
    
print(', '.join(names)) # preferable when joining more than 2 or more strings

import os

location_of_files = "/home/saif/learn/notes/python/sentdex_tuts/intermediate"
file_name = "1_intro.txt"

print(location_of_files + '/' + file_name) # not the correct way but works

# proper method of joining for file paths/location
with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())


## Formatting
who = "Gary"
how_many = 12

# Gary bought 12 apple today!

# this is not the most optimal way of doing this.
# in python2 we could have used something like %s etc.
print(who, "bought", how_many, "apples today!")

# In python 3 we use {} combined with format()
print("{} bought {} apples today!".format(who, how_many))
# you can also give order sqeuence
print("{1} bought {0} apples today!".format(who, how_many))
