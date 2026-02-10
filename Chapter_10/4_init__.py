
class Employee():
    language = "Python"
    Salary = "1,00,000"
    
    def __init__(self):    #Dunder method which is automatically called 
        print("I am creating a object ")
        
    def getInfo(self):
        print(f"Language is {self.language} \nsalary is {self.Salary}")
    
Ranjan = Employee()
Ranjan.name = "Ranjan"  
print(Ranjan.name,"\n",Ranjan.Salary)   
