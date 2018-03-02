# Statistics module

'''
' The statistics module comes with python 3 and provides quality of life
' fundamental math functions
'''

import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

# Mean (average of the numbers)
x = statistics.mean(example_list)
print(x)

# Median (the middle value)
y = statistics.median(example_list)
print(y)

# Mode (value which has highest frequency)
z = statistics.mode(example_list)
print(z)

# Standard Deviation (i.e. sq. rt. of Variance)
a = statistics.stdev(example_list)
print(a)

# Variance (i.e avg. of the squared diff from the mean)
b = statistics.variance(example_list)
print(b)
