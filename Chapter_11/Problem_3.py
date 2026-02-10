# Create a class Employee and add salary and increment properties to it 
# Write a salaryafterincrement methodwith a @property decorator with a setter
# Which changes the value of increment based on the salary

class Employee:
    salary = 1200
    increment = 50
    
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.salaryafterincrement = ((salary/self.salary) - 1) * 100

E = Employee()
print(E.salaryafterincrement)
print(E.increment)