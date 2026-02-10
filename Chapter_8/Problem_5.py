# WAP to print * in order using recursion

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

n = int(input("Enter the lines : "))
pattern(n)