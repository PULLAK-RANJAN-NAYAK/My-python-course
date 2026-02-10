# Use of the property and setter decorator

class Employee:
    a = 1   # Class attribute

    @classmethod
    def show(cls):
        # Accesses class attribute
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        # Acts like a getter method
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        # Acts like a setter method
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()

e.name = input("Enter your name : ")  # Calls name.setter
print(e.name)                         # Calls @property (getter)

e.a = 45      # Instance attribute (does not affect class attribute)

e.show()      # Still prints class attribute
