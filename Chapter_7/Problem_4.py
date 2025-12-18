# Check whether the given numbers are prime

n = int(input("Enter your number : "))

for i in range(2,n):
    if(n%i)== 0:
        print("The number is not prime")
        break
else:
    print(f"Number is prime : {n} ")