# Classes and instances

'''
Classes can be seen throughtout most modern programming languages.
They allow us to write reusable code. Data and function associated with a
specific class are called attributes and methods respectively.

Lets create a simple Employee class.

A class is a blueprint for creating instances so each unique employee that we
create using the Employee class will be an instance of the Employee class.

There is an important difference between class and instance variables, here we
will focus on instance variables, which contain data unique to each instance.
'''


# class Employee:
#     pass


# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# # We can add attributes on the fly
# emp_1.first = "Saif"
# emp_1.last = "Azmi"
# emp_1.email = "saif.azmi@example.com"
# emp_1.pay = 60000

# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "test.user@example.com"
# emp_2.pay = 50000

# print(emp_1.email)
# print(emp_2.email)

'''
The code above works, but its not the best use of a class. We will now use
a the special dunder __init__ method, this method can be thought of as a
constructor in other languages or simply as initialise.

When we create methods within a class they receive the instance as the first
argument automatically and by convention we should call it "self", essentially
self represents the instance.

If we forget to pass "self" to a class method it will result in an error when
trying to use that method.
TypeError: fullname() takes 0 positional arguments but 1 was given

The error message can be confusing as it doesn't look like that we are passing
any arguments into the function, but the instance is getting passed
automatically hence the first self argument.
'''


class Employee:

    def __init__(self, first, last, pay):
        self.first = first  # the self.var doesn't need to be the same as var
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


# The __init__ method will be run automatically
emp_1 = Employee("Saif", "Azmi", 60000)
emp_2 = Employee("Test", "User", 50000)

# We can display the full name directly by accessing the attributes
print("{} {}".format(emp_1.first, emp_1.last))

# Using the class method
print(emp_2.fullname())
# The code line above gets tranformed into the following line of code
print(Employee.fullname(emp_2))
