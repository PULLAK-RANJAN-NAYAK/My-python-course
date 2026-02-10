# Use of class method decorator

class Employee:
    a = 1   # Class attribute

    @classmethod
    def show(cls):
        # cls refers to the class, not the object
        print(f"The class attribute of a is {cls.a}")


e = Employee()

e.a = 45    # Instance attribute (does not change class attribute)

e.show()    # Accesses class attribute using cls
