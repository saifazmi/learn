# Function Parameters

def simple_addition(num1, num2):
    answer = num1 + num2
    print("num1 is", num1)
    print(answer)

simple_addition(5,3)

'''
' The quantity of parameters and
' The order in which parameters are passed to a function matters
' But we can explicitly identify the value of each parameter
'''

simple_addition(num2=3, num1=5)
