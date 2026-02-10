# Inheritance means one class acquires the properties and methods of another class.

# Parent class
class Employee:
    company = "FAANG"
    name = "Default"

    def show(self):
        print(f"The name is {self.name} and the language is {self.company}")


# Another parent class
class coder:
    language = "Python"

    def printlanguage(self):
        print(f"The language of the Employee is {self.language}")


# Child class inheriting from Employee and coder (multiple inheritance)
class Programmer(Employee, coder):
    company = "ITC infotech"

    def showlanguage(self):
        print(f"The comapny is {self.company} works on {self.language}")


# Creating objects
a = Employee()
b = Programmer()

# Calling methods
a.show()
b.showlanguage()
b.printlanguage()
