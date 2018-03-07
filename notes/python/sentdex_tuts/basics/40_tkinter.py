# Tkinter introduction

'''
' Tkinter is part of the standard library in python
' this module is a wrapper around tk which is a wrapper around tcl
' tcl is what actually creates windows and gui
'
' Because of all these wrapper, we can create a very simple window with
' only a few lines of code (~ 8 lines), which would otherwise require a lot
' of code.
'
' The anatomy of a window consists of the parent frame containing the window
' and everything else goes inside that frame
'''

from tkinter import *

'''
' create a window class i.e. master widget
' Here, we are creating our class, Window, and inheriting from the Frame
' class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
'''

class Window(Frame):

    # this defines the main/parent window and everything else goes in here
    def __init__(self, master = None):
        Frame.__init__(self, master) # initialise the frame
        self.master = master

root = Tk() # root window

app = Window(root) # create instance of the window

root.mainloop() # show the window and begin the main loop
