#Check wheather the entered name are in the list

list = ["Pullak","Ranjan","Nayak","Smonarxh"]

name = input("Enter your name : ")

if(name in list ):
    print("Your name is in the list",name)
else:
    print("Invalid person!")