# The difference between the instance attribute and class attribute

class Employee():    # This is class attribute
    language = "Python"
    Salary = "1,00,000"
    
Ranjan = Employee()
Ranjan.language = "AI"      # This is an instance attribute
print(Ranjan.language,Ranjan.Salary)

# Instance attribut takes the preference over class attributes during 
# assignments and retrieval