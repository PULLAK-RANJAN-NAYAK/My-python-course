## Multilevel inheritance means a class is derived from another derived class,
# forming a chain where each child inherits from its parent.

# Base class
class Employee:
    a = 1

# Derived from Employee
class coder(Employee):
    b = 2

# Derived from coder (multilevel inheritance)
class manager(coder):
    c = 3

# Object of Employee
o = Employee()
print(o.a)   # Accessing Employee variable

# Object of manager
o = manager()
print(o.a, o.b, o.c)   # Accessing variables from all levels
