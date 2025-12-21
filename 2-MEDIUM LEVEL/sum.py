# Write a program to find the sum of the numbers 

n = int(input("Enter the number : "))

total = 0

while n>0:
    digit = n % 10
    total = total + digit
    n = n // 10
print(total)
