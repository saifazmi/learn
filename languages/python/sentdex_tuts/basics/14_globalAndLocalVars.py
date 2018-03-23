# Global and Local Variables

'''
' Scope is the reach of a variable within a script or a program
' GLOBAL: Can be accessed anywhere
' LOCAL: Can be accessed within its environment/frame/code block
'''

x = 6 # Committed to memory before any other operations are called
z = 10
def example():
    global x
    print("x =", x) # We have access to the variable
    print("x+5 =", x+5) # It can be modified

    x += 6 # This will give error without the global keyword
    print("x += 6:", x)
    '''
    ' But when performing operations directly on the variable like above
    ' an "UnboundLocalError: local variable 'x' referenced before assignment"
    ' error message is thrown. Because the problem is that "x" in this case is
    ' NOT a Global Variable.
    '
    ' The easiest thing to do is to deifne "x" as
    ' a global variable usinng the keyword "global"
    '''
    globZ = z
    globZ += 10
    return globZ

'''
' To completely avoid using global variables in your program i.e. using the
' "global" keyword, based on programming constraints of not using a global var
' You can assign the value of the global var to a local var in the function and
' return and save it in the var outside.
'''
print("z =", z)
z = example()
print("z = example():", z)
