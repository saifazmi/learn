# Headless Error Handling

'''
' In smaller programs it is easy to find where things went wrong based on the error
' message, but they become less helpful as your program grows and expands to 1000s of
' lines of code and multiple files
'
' We can use "sys" module to make these error messages more helpful, and can be combined
' with the "logging" module
'''

import sys
import logging

try:
    a+b
except Exception as e:
    #print(str(e))
    # name 'a' is not defined
    print(sys.exc_info())
    '''
    ' (<class 'NameError'>, NameError("name 'a' is not defined",),
    ' <traceback object at 0x7fb1bd754f48>)
    '
    ' We already get a tuple with a lot more information, we can slice this up
    '''
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2].tb_lineno) #<traceback object at 0x7f6c47190248>.tb_lineno
    '''
    ' <class 'NameError'>
    ' name 'a' is not defined
    ' 14
    '
    ' Its unwise to save these these values to variables as it can result in circular
    ' reference if there is an exception within an exception. Resulting in NO garbage
    ' collection for these variables
    '''

    print("Error: {}. {}, line: {}".format(sys.exc_info()[0],
                                           sys.exc_info()[1],
                                           sys.exc_info()[2].tb_lineno))
    # Error: <class 'NameError'>. name 'a' is not defined, line: 14

    '''
    ' The error message above is a log more useful compared to what we had earlier
    '''

'''
' Lets combine this with logging methods
'''

def error_handling():
    return "{}. {}, line: {}".format(sys.exc_info()[0],
                                           sys.exc_info()[1],
                                           sys.exc_info()[2].tb_lineno)

try:
    a+b
except Exception as e:
    logging.error(error_handling())


a+b
'''
Traceback (most recent call last):
  File "/home/saif/learn/notes/python/sentdex_tuts/intermediate/13-21_OOPs/23_errorHandling.py", line 11, in <module>
    a+b
NameError: name 'a' is not defined
'''
