# More on list comprehension and generator expressions


'''
' Let's show a more realistic use case for generators and list comprehension:
'''

input_list = [5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# building a generator using if statement
xyz = (i for i in input_list if div_by_five(i))

### The code above is logically same as the following
##xyz = []
##for i in input_list:
##    if div_by_five(i):
##        xyz.append(i)

##for i in xyz:
##    print(i)

# Short hand for the code above
[print(i) for i in xyz]

print(xyz) # generator expression

# building a list using if statement
xyz = [i for i in input_list if div_by_five(i)]
print(xyz) # now its a list
[print(i) for i in xyz]

print(10*'#')

## Embedding

# list comp
[[print(i,ii) for ii in range(5)] for i in range(5)]

# The line of code above is identical to:
##for i in range(5):
##    for ii in range(5):
##        print(i,ii)

# creating tuples
xyz = [[(i,ii) for ii in range(5)] for i in range(5)]
print(xyz)

# creating lists
xyz = [[[i,ii] for ii in range(5)] for i in range(5)]
print(xyz)

# generator exp
xyz = (((i,ii) for ii in range(5)) for i in range(5))
print(xyz)

for i in xyz:
    print(i)
    for ii in i:
        print(ii)

print(10*'#')

## Extra
# doesn't print anything because its a genexp, converting to list comp works
(print(i) for i in range(5))

# But we can do this
xyz = (print(i) for i in range(5))

for i in xyz:
    i # because every i in xyz is a print(i)
