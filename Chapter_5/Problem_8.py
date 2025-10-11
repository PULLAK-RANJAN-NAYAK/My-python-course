# What if the value is same for 2 keys 

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
#     Enter friends name : Pullak
# Enter favourite language : Python
# Enter friends name : Ranjan
# Enter favourite language : Python
# Enter friends name : Nayak
# Enter favourite language : C
# Enter friends name : Smonarxh
# Enter favourite language : C++
# {'Pullak': 'Python', 'Ranjan': 'Python', 'Nayak': 'C', 'Smonarxh': 'C++'}

# Nothing happens if the value is same for 2 keys 