# Write a program top print fibonacci series

# What is Fibonacci?
# Each number is the sum of the previous two.

n = int(input("Enter the terms : ")) #Don"t go putting many terms it is just for the range 

a = 0
b = 1

print(a)
print(b)

for i in range(0,n+1):
    c = a + b
    print(c)
    a = b
    b = c