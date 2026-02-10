# Inheritance means one class acquires the properties and methods of another class

# Parent / Base class
class Employee:
    # Class variable (common for all employees)
    company = "FAANG"
    
    # Method to show employee details
    def show(self):
        # self refers to the current object
        print(f"The name is {self.name} and the salary is {self.salary}")
    

# Child / Derived class
# Programmer inherits from Employee
class Programmer(Employee):
    # This class has its own company value
    company = "ITC infotech"
    
    # Method specific to Programmer class
    def showlanguage(self):
        print(f"The language of the employee is {self.language}")
    

# Creating an object of Employee class
a = Employee()

# Creating an object of Programmer class
b = Programmer()

# Accessing company variable using Employee object
print(a.company)   # Output: FAANG

# Accessing company variable using Programmer object
# Programmer's company overrides Employee's company
print(b.company)   # Output: ITC infotech
