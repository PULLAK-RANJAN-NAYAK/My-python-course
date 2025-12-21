# Write a program to find factorial of an number 

n = int(input("enter an number : "))
product = 1

for i in range(1,n+1):
    product = product*i
print(f"The factorial is : {product}")
