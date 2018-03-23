# Function Parameter Defaults

def simple(num1, num2):
    pass

# assigning a default value to num2
def simple(num1, num2=5):
    print(num1, num2)


'''
' Even though the function requires 2 parameters, we can pass just one
' because the other parameter is defined by default
'''
simple(2)


def basic_window(width, height, font="TNR",
                 bgc='w', scrollbar=True):
    print(width, height, font, bgc)


'''
' When there are multiple parameters like in the example above, passing values
' to function's default or named parameters is done by using their names
'''
basic_window(500,350,bgc='b')
