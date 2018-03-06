# Matplotlib plotting from CSV files

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np # generally imported as np

style.use("ggplot")

'''
' How to import CSV files? there are many options, we can use open() or
' the built-in csv module. But here we will be using NumPy, again not part of
' the stdlib, so needs to be downloaded via pip
'''

# This function can loads both csv and txt, dont be confused by the name
# unpacking values
x,y = np.loadtxt("exampleFile.txt",
                 unpack = True, # important else data will be list of list
                 delimiter = ',')
'''
' It's important to note here that you MUST unpack the exact same number
' of columns that will come from the delimiter that you state.
' If not, you'll get an error.
'''

# print(x)
# print(y)

'''
' The data looks like this after unpacking:
' [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16.]
' [ 5.  7.  8.  3.  5.  6.  3.  7.  2. 12.  5.  7.  2.  6.  9.  2.]
'
' These don't look like a typical python list, because these are NumPy Array.
' Generally these are converted into a python list and then converted back.
'''

plt.plot(x,y)

plt.title("Epic Chart")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()
