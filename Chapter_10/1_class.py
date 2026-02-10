# This program demonstrates a basic use of Class and Object in Python
# along with lists and looping.
# Concept covered: Class variables, Object creation, Indexing, Loop

class Employee:
    # Class variables (shared by all objects of the class)
    name = ["Ranjan", "Pullak", "Nayak"]
    technology = ["Python", "AI", "LLM"]
    salary = ["1,00,000", "1,20,000", "1,50,000"]


# Creating an object of the Employee class
Company = Employee()

# Looping through the list using index
for i in range(3):
    # Printing employee details one by one
    print("Name:", Company.name[i])
    print("Technology:", Company.technology[i])
    print("Salary:", Company.salary[i])
    print()  # Blank line for better readability


# A class is a template that contains:
# 1. Variables (data)
# 2. Methods (functions)