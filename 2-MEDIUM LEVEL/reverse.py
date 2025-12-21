#Write a program to reverse an number 

n = int(input("Enter your number : "))

rev = 0

while n>0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)    
