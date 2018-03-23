'''
' There are 2 loops in python3 logic, "for" and "while" loops.
' Both of them an be used interchangeably and depends on either
' programmer preference or reliant on efficiency.
'
' Generally FOR loop can be more efficent than while loop, BUT not always.
' While loop is typically used as a counter
'''

# While Loop

condition = 1

while condition < 10:
    print(condition)
    condition += 1 # python allows short hand syntax

# Infinite loop example
while True:
    print("doing stuff")
