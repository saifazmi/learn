# More on Generators i.e. Building your own generator

'''
' These are proper generators and not just generator expressions
' A generator doesn't return anything
'''

# A simple generator function
def simple_gen():
    yield "Oh"
    yield "hello"
    yield "there"


for i in simple_gen():
    print(i)

## Example of a password cracker
CORRECT_COMBO = (3, 6, 1)

##found_combo = False # to break every loop
##for c1 in range(10):
##    if found_combo:
##        break
##    for c2 in range(10):
##        if found_combo:
##            break
##        for c3 in range(10):
##            if (c1, c2, c3) == CORRECT_COMBO:
##                print("Found the combo: {}".format((c1, c2, c3)))
##                found_combo = True
##                break # only breaks out of one for loop
##            print(c1,c2,c3) # running past even after findings the combo

'''
' The for loops above has a lot of code with lot of moving parts and breaks,
' not very efficient and simply ugly!
' So lets make a generator
'''

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2 ,c3) == CORRECT_COMBO:
        print("Found the combo: {}".format((c1, c2, c3)))
        break
    print(c1,c2,c3)
