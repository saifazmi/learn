# Matplotlib labels

from matplotlib import pyplot as plt

'''
' generally data will be pulled from external resources as list and stored
' in variables, so its better to assign values like this
'
' A common error that might occur when assigning values with lists
' ValueError: x and y must have same first dimension
' This occurs when length of list x and y is not the same
'''

x = [5,6,7,8]
y = [7,3,8,3]

plt.plot(x,y)

'''
' We need to add titles and labels to our charts
'''

plt.title("Epic Chart")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()
