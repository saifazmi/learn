# Intro to Object Oriented Programming in Python

'''
' Using pygame to learn OOPs as it provides visual representation of objects
' which makes it easier to understand OOPs concepts
'''

# This is a class definition
class Blob:
    '''
    ' This is the initialiser, "self" is an instance object shared throughout
    ' the class, it can have any name, but self is the norm and is used for
    ' accessing an object's attributes from with the class, as well as outside
    ' the class, where object variable names takes the place of "self"
    ' The initialiser runs when the object of this class is created
    ' same as a java constructor?
    '''
    def __init__(self, color):
        # attributes of the class object
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.rangrange(4,8) # not sure of the metric
        self.color = color

    # Method
    def move(self):
        self.move_x = random.randrange(-1,2) # pixel movement
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH

        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT
