# Write a program to check whether the number is prime or not 

n = int(input("Enter your number : "))

for i in range(2,n):
    if(n%i) == 0:
        print("Entered number is not prime")  
        break     
else:
    print(f"{n} is prime")
    
    