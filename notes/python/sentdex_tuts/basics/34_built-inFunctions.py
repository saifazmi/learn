# Built-in function and standard libs

exNum1 = -5
exNum2 = 5

# Returns the absolute value of a number
print(abs(exNum1))

if abs(exNum1) == exNum2:
    print("these are the same")

# help() function lets you get the documentation for a module
# >>> help() will return a prompt to search the doc of any module
# >>> help("time") will return the doc of time module
# >>> import time
# >>> help(time) if the module is not passed as a string it will give an error
# BUT if we import the module before calling it with the help() it will work

# Maximum and Minimum functions
exList = [5,6,3,7,8,0]
print(exList)
print(max(exList))
print(min(exList))

# Rounding values
x = 5.622
y = 5.222
print(round(x)) # rounds up
print(round(y)) # rounds down

# Floor and Ceil will also do the rounding
# But they are part of the math library
import math
print(math.floor(x)) # always rounds down
print(math.ceil(x)) # always rounds up

# Converting data types
intMe = "55"
print(intMe)
print(int(intMe))
print(float(intMe))

strMe = 77
print(strMe)
print(str(strMe))
