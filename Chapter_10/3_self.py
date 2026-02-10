
class Employee():
    language = "Python"
    Salary = "1,00,000"
    
    def getInfo(self):      # The self is a variable 
        print(f"Language is {self.language} \nsalary is {self.Salary}")
    
Ranjan = Employee()         # Ranjan is an object, both self and Ranjan are same
Ranjan.getInfo()