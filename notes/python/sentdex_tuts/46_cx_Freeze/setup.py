'''
' This file tells cx_Freeze how to build the exe file
'''

from cx_Freeze import setup, Executable

setup(name = "urlParse", # name of the executable
      version = "0.1", # version of the exe
      description = "Parse stuff",
      executables = [Executable("distme.py")]) # list of executable sources

'''
' Now run this file by using the following command in the terminal
' $ python setup.py build
'
' this creates a "build" folder which will contain the executable
'''

'''
' As a side note, it has been pointed out to me on sentdex's discord server
' that "pyinstaller" is a much better option and seems like it, as the setps
' are straight forward.
'
' $ pip install pyinstaller
' $ pyinstaller yourprogram.py
'''
