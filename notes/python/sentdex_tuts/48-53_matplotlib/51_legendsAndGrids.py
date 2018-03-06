# Matplotlib labels and grid lines

from matplotlib import pyplot as plt

x = [5,6,7,8]
y = [7,3,8,3]

x2 = [5,6,7,8]
y2 = [6,7,2,6]

plt.plot(x,y, 'g', linewidth=5, label = "Line One") # assigning labels
plt.plot(x2,y2, 'c', linewidth=10, label = "Line Two")

plt.title("Epic Chart")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend() # display legends, call AFTER plotting what needs to be in legend
plt.grid(True, color='k') # display grid, black in color

'''
' things are displayed in the order they are called, for example line 2 draws
' over line 1 as we are ploting them in that order.
' But a grid line will always be drawn behind everything else, no matter when
' and where the function is called.
'''

plt.show()
