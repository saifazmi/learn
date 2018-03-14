# Special (Magic/Dunder) methods in classes

'''
A simple usecase of special methods is to implement operator overloading
or to define the string representation of an object.

The most common special method that we encounter when working with classes is
the __init__ method. Some other common special methods that we should almost
always implement are __repr__ and __str__

__repr__ is an debugging/developer friendly representation of the object
__str__ is the more human readable rep of an object for end-users

__repr is the fallback method if there is no __str__ method, so its good to
have __repr__ at the minimum.

A good rule of thumb for creating __repr__ is to try and display something that
can be copy and pasted back in to python code to recreate that object.

There are dunder methods for arithematic opoerations like __add__, __mul__, etc
'''


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first,
                                                 self.last,
                                                 self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # When adding two employees, return combined pay
    def __add__(self, other):
        return self.pay + other.pay

    # The length of employee's fullname
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Saif', 'Azmi', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)  # uses the __str__ method

print(repr(emp_1))  # specifically getting the value of __repr__ method
print(str(emp_1))  # getting the value of __str__ method

# The print statements above are same as the following:
print(emp_1.__repr__())
print(emp_1.__str__())

print(1 + 2)  # uses the special __add__ of int object in the background
print(int.__add__(1, 2))

print('a' + 'b')  # __add__ of str object
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)  # using the __add__ of Employee class

print(len("test"))  # __len__ of str object
print("test".__len__())

print(len(emp_1))  # __len__ of Employee class
