# Class Variables

'''
A class variable is shared amongst all instances of a class which is the
opposite to the uniqueness of instance variables

Class vars need  to be accessed using the class name or instance, else error
NameError: name 'raise_amount' is not defined

When try to access an attribute on an instance the first check is to see if
that instance has that attribute, then the class and then any inherited class.
This makes using the class name vs self when accessing class variables crucial.

If a class var is modified for a specific instance as seen in the example below
it is important to use self.<classVar> to use the modified value, since using
the <className>.<classVar> access method will return the old classVar value.
'''


class Employee:

    num_of_emps = 0
    raise_amount = 1.04  # abstracting out the raise amount as class var

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Saif", "Azmi", 60000)
emp_2 = Employee("Test", "User", 50000)

Employee.raise_amount = 1.05  # changes the value for class and instances
emp_1.raise_amount = 1.06  # changes value for the instance only

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Lets print the namespaces to see what they have
print(emp_1.__dict__)  # contains the custom raise_amount for the instance
print(emp_2.__dict__)  # doesn't have raise_amount
print(Employee.__dict__)  # contains raise_amount

print(Employee.num_of_emps)
