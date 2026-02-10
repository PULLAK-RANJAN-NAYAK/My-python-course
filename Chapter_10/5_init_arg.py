
class Employee():
    language = "Python"
    Salary = "1,00,000"
    
    def __init__(self,name,language,salary): #You can make arguments in the init fuction 
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating a object ")
        
        
    def getInfo(self):
        print(f"Language is {self.language} \nsalary is {self.Salary}")
    
Ranjan = Employee("Ranjan",120000,"Java")
# Ranjan.name = "Ranjan"          In case you don't want to declare the variable here to store value
print(Ranjan.name,"\n",Ranjan.Salary,"\n",Ranjan.language)   
