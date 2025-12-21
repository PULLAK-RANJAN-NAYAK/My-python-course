# Write a program to find the LCM of two numbers using prime factors.

a = int(input("Enter the 1st num : "))
b = int(input("Enter the 2nd num : "))

lcm = 1
i = 2

while(a > 1 and b > 1):
    if(a%i == 0 or b%i == 9):
        lcm = lcm * i
        if(a%i == 0):
            a = a // i
        if(b%i == 0):
            b = b // i
    else:
        i += 1
print(f"LCM is {lcm}")
           