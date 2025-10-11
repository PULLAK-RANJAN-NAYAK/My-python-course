# How to take input from the user

a = input("enter num 1 : ")
b = input("enter num 2 : ")
print("a is : ",a) 
print("b is : ",b)

#Lets add the variable
a = input("enter num 1 : ")
b = input("enter num 2 : ")
print("a is : ",a) 
print("b is : ",b)
print("sum is :",a+b)#so basically if you don't actually define the data type it is going to concatinate like 3 + 4 = 34

#lets give them the data type
a = int(input("enter num 1 : "))
b = int(input("enter )num 2 : "))
print("a is : ",a) 
print("b is : ",b)
print("sum is :",a+b)#done 3+5=8
c = float(a+b)
d = type(c)
print(d)