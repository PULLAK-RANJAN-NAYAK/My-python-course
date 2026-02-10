# Use the super() constructor to call the parent class constructor

class Employee:
    def __init__(self):
        print("This is the employee constructor")
    a = 1


class coder(Employee):
    def __init__(self):     #--> If you add the super constructor it will run the Employee as Employee 
        print("This is the coder constructor")                  # class is it's parent
    b = 2


class manager(coder):
    def __init__(self):
        super().__init__()   # Calls coder's constructor
        print("This is the manager constructor")
    c = 3


# Creating Employee object
o = Employee()
print(o.a)

# Creating manager object
o = manager()
print(o.a, o.b, o.c)
