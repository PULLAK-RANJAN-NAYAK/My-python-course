# Write a program to find the lcm of the entered digit 

a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

n = max(a,b)

while True:
    if (n%a == 0 and n%b == 0):
        lcm = n
        break
    n+=1

print(f"LCM of {a} and {b} is {lcm}")
       