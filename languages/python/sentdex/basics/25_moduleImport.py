# Module Import syntax

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

'''
' Using the "as" keyword we can import a module and assign it an abbriviated
' reference.
'''
import statistics as s

x = s.variance(example_list)
print(x)

'''
' We can also import specific functions from a module using the "from" keyword
' and use it directly, without referencing the module name
'''
from statistics import stdev

y = stdev(example_list)
print(y)

'''
' The two features mentioned above can be combined to pick a specific function
' and then abbriviate it.
'''
from statistics import variance as v

z = v(example_list)
print(z)

'''
' It is also possible to pull out multiple functions from a module and they
' can both still be abbrivated by using the "as" keyword for each function
'''
from statistics import mean as me, mode as mo

a = me(example_list)
print(a)

b = mo(example_list)
print(b)

'''
' If we want to import everything but don't want to use the module reference
' we can use "*" to import everything and use them directly
'''
from statistics import *
# Median has not been imported in any of the imports before
c = median(example_list)
print(c)

