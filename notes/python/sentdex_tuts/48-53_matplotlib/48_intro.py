# A matplotlib crash course

'''
' The module is not a part of the standard library
'
' for basic ploting we use "pyplot"
' the basics follows, plot, draw and show sequence
'''

# Most people import as plt
from matplotlib import pyplot as plt

# plt.plot(5,6) # x,y
plt.plot([5,6,7,8],[7,3,8,3]) # [x],[y] / this won't display the graph

'''
' when doing live graphs we will have to use the draw function to redraw
' and then use show to update
'''

plt.show() # displays the graph
