# Write a program to find the greatest of the three numbers using functions 

def greatest(a, b, c):
    if a > b and a > c:
        print("A is greatest")
    elif b > a and b > c:
        print("B is greatest")
    elif c > a and c > b:
        print("C is greatest")
    elif a == b == c:
        print("All are same")
    else:
        print("Invalid input")

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))

greatest(a, b, c)
