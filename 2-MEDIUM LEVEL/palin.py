# Write a program to find whether the number is palindrome or not 

# What is a Palindrome?
# A number is a palindrome if it reads the same forward and backward.

n = int(input("Enter the number : "))

temp = n
rev = 0

while (n > 0):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if(temp == rev):
    print("Entered number is palindrome")
else:
    print(f"{temp} Is not palindrome")