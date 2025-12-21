# Write a program to find whether the entered number is armstrong number or not

# What is an Armstrong number? (simple)
# A number is an Armstrong number if:
# Sum of each digit raised to the power of number of digits = original number

n = int(input("Enter the number : "))

temp = n
sum = 0
 
while(n > 0):
    digit = n % 10
    sum = sum + (digit * digit * digit)
    n = n // 10
if(temp == sum):
    print("Entered number is armstrong")
else:
    print("Entered number is not armstrong")

