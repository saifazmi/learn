# Variable Examples

# Camel Casing, personal preference
exampleVar = 55
print(exampleVar)

# Underscore
# Can store operations
example_var = 55 + 32
print(example_var)

# All caps, generally for constants
# Variable names are case sensitive so this will not overwrite the previous var
# Can also store functions return values
EXAMPLE_VAR = type("hey!")
print(EXAMPLE_VAR)

# Unpacking variables
# Example coordinates, unpacking a python list into x,y
x,y = (3,5)
print(x)
print(y)
# x,y = (3,5,8) will FAIL as there are not enough var to unpack into.
