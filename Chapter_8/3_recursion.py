#A program to print the factorial of a number using recursion

def factorial(n):
    if(n==1 or n==0):
        return 1  #This is the base case as if the entered n value is 1 or 0 then it will return 1
    return n * factorial(n-1) #this is the recursion function it calls the function itself to calculate the factorial

#This is the main function that calls the factorial function you can do it above the function but it is good to keep it below the function
n = int(input("Enter the number: "))
print(f"The factorial of {n} is : {factorial(n)}")     

# You need to be extremely carefull so that the functions doesn't call itself infinitely

# Hope this helps you understand the recursion function and how it works