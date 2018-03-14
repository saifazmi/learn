# Difference between regular, class and static mehtods

'''
CLASS METHODS
==============
If a regular method automatically takes in the instance as the argument, we can
turn it into a class method we can use the @classmethod decorator which passes
the class as the first argument and call it "cls" by convention.

Class methods can be run from an instance but it doesn't make much sense and is
not used very often.

Somme people use class methods as alternative constructors, i.e. you can use
these methods to provide multiple ways of creating the objects.
These alternative constructors start with "from_" as a convention.
For an example of real world implementation of alt const checkout datetime
module in python

STATIC METHODS
===============
Easily confused with class methods, but static methods don't pass anyting as
automatic arguments like self or cls. So they behave just like regular
functions except we include them in classes because they have some logical
connection with the class.

They are declared using the @staticmethod decorator.

We generally end up writting regular methods whcih should be static methods, to
identify such methods check if we don't access the instance or class anywhere
within the method.
'''


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Alt constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Saif", "Azmi", 60000)
emp_2 = Employee("Test", "User", 50000)

Employee.set_raise_amt(1.05)  # updates the raise_amount class variable

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Lets assume that most of our data comes int he following format
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

# We can use these line of code to process the data and then create an employee
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

# If the above is a common usecase then we can create an alt constructor for it
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))  # False
