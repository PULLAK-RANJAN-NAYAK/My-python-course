# What if 2 keys are same then what happens

d = {}

name = input("Enter friends name : ")
language = input("Enter favourite language : ")
d.update({name : language})
name = input("Enter friends name : ")
language = input("Enter favourite language : ")
d.update({name : language})
name = input("Enter friends name : ")
language = input("Enter favourite language : ")
d.update({name : language})
name = input("Enter friends name : ")
language = input("Enter favourite language : ")
d.update({name : language})

print(d)

# Output :
#   Enter friends name : Pullak
# Enter favourite language : Python
# Enter friends name : Pullak
# Enter favourite language : C++
# Enter friends name : Ranjan
# Enter favourite language : C
# Enter friends name : Nayak
# Enter favourite language : Java
# {'Pullak': 'C++', 'Ranjan': 'C', 'Nayak': 'Java'}
# The update button is going to update the value as the output is given above