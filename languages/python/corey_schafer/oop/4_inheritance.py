# Inheritance - Creating Subclasses

'''
Class inheritance allows us to inherit attributes and methods from a parent
class. This useful because we can create subclasses with all the functionality
of parent class and modify or add new methods and attributes without changing
the parent class.

Lets say we want to create different types of Employees eg: developers and
managers.

Just by inheriting the parent class we get everything from it

class Developer(Employee):
    pass

dev_1 = Developer("Saif", "Azmi", 60000)
dev_2 = Developer("Test", "User", 50000)

The code will create the developer employees even though the Developer class
doesn't have a __init__ method of it own. When creating these Developer, python
first looks in the Developer class for init method since its not there, python
walks up the chain of inheritance and reaches the Employee class and looks for
the init method there and since that exists, it is used. Python follows this
chain until it encounters what it needs and this chain is called:
The Method Resolution Order

A real world example of inheritance and subclasses is the python exception
module of WSGI library
'''


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@email.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):

    raise_amount = 1.10  # Update the raise_amount for this class only

    def __init__(self, first, last, pay, prog_lang):
        # using the init method of parent class, works well for single inherit
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Saif", "Azmi", 60000, "Python")
dev_2 = Developer("Test", "User", 50000, "Java")

# print(help(Developer))  # prints the method resolution order
'''
class Developer(Employee)
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
'''

print(dev_1.email)
print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

# Instance and Class  related built-in functions
print(isinstance(mgr_1, Manager))  # True
print(isinstance(mgr_1, Employee))  # True
print(isinstance(mgr_1, Developer))  # False

print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Developer))  # False
