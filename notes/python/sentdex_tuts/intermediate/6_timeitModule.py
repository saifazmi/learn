# Timeit module

'''
' Measures the amount of time it takes for a snippet of code to run
' Why do we use timeit over something like start = time.time()
' total = time.time() - start
'
' The above is not very precise as a background process can disrupt the snippet
' of code to make it look like it ran for longer than it actually did.
'''

import timeit

# print(timeit.timeit("1+3", number=500000000))

##input_list = range(100)
##
##def div_by_five(num):
##    if num % 5 == 0:
##        return True
##    else:
##        return False
##
##xyz = (i for i in input_list if div_by_five(i))
##
##xyz = [i for i in input_list if div_by_five(i)]


## Timing creation of a generator expression
print("Gen Exp:", timeit.timeit("""
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))
""", number=5000))

## Timing creation of a list comprehension
print("List Comp:", timeit.timeit("""
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = [i for i in input_list if div_by_five(i)]
""", number=5000))

## Timing iterating over a genexp
print("Iter GenExp:", timeit.timeit("""
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

for i in xyz:
    x = i
""", number=500000))

## Timing iterating over a list comp
print("Iter ListComp:", timeit.timeit("""
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = [i for i in input_list if div_by_five(i)]

for i in xyz:
    x = i
""", number=500000))
