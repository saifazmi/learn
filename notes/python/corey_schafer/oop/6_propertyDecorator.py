# Property Decorators - Getter, Setters and Deleters

'''
The property decorator allows us to give our class attributes getter, setter &
deleter functionality like other programming languages.

@property decorator lets us define methods that can be accessed as an attribute
This is very helpful as we can convert pre-existing attributes to methods
without breaking old code bases that are using the older version of the class

@functionName.setter decorator lets us create a setter method
@functionName.deleter decorator lets us create a del operator for the instance
'''


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    # Getter
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # Setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Deleter
    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")

emp_1.first = "Jim"

emp_1.fullname = "Saif Azmi"

print(emp_1.first)
print(emp_1.email)  # accessing like an attribute
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)
