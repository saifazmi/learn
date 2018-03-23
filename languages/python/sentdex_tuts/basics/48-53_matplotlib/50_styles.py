# Matplotlib styles

from matplotlib import pyplot as plt
from matplotlib import style

'''
' The syles are a *.mlstyle file which is similar to a stylesheet
' in functionality, the style module comes with some pre-installed styles
' and we can also install extras or make our own custom version
'''

style.use("ggplot")

x = [5,6,7,8]
y = [7,3,8,3]

x2 = [5,6,7,8]
y2 = [6,7,2,6]

'''
' Changing the colors without using style
'''
plt.plot(x,y, 'g', linewidth=5) # green
plt.plot(x2,y2, 'c', linewidth=10) #cyan

plt.title("Epic Chart")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()
