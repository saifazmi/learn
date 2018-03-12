# Special Methods, OOP and iteration

'''
' Bringing things together in this program
'''


# x = range(5)

# Is there a deifference b/w this "x" and the one above?
x = (i for i in range(5))

# Rather than using a for loop to iterate, we can use next()
next(x)
x.__next__()

'''
' next() manually moves the iterator one at a time,
' an iterator does dis automatically by going over an iterable and hiting next
' until stop iterator is hit
'
' All next is doing is that its calling the dunger __next__ method of "x" object
' This tells us that everything in python is an Object i.e. python is an
' Object Oriented Language.
'''

for i in x:
    print(i) # 2, 3, 4 ; because we used next() twice before this
print(10*'#')

'''
' We can use dir(object) method to find all the valid
' method of an object
'
' >>> dir(x)
' ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__',
' '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
' '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__',
' '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__',
' '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
' 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
'
' We can choose to overwrite any of these python provided dunder methods
' for the object
' Lets create our own iterator class
'''

class range_examp:
    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val


x = range_examp(5)

x.__next__()
next(x)

for i in x:
    print(i)
print(10*'#')

for i in range_examp(5):
   print(i)
print(10*'#')


'''
' What if we define our own generator which is not range()
' the yield ability is the key here which is not like return a yield will
' let you continue after yielding the value but a return will end the function
'''

def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1

for i in range_gen(5):
    print(i)
print(10*'#')

x = range_gen(5)

for i in x:
    print(i)
print(10*'#')


'''
' To answer the difference between a range(5) and (i for i in range(5))
' 
' >>> dir(range(5)) ## NO __next__ method for iteration since "yield" is used
' ['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
' '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
' '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
' '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
' '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
' 'count', 'index', 'start', 'step', 'stop']
'
' dir((i for i in range(5))) ## Has a __next__ method for iteration
' ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__',
' '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
' '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__',
' '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
' '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code',
' 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
'''
