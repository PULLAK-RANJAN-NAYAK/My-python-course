# WAP to print multiplication table using function

def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter number : "))

multiply(n)