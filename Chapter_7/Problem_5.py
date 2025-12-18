# Sum all the natural number the range entered by the user using while loop

n = int(input("Enter your range : "))

i = 1
sum = 0

while(i<=n):
    sum += i 
    i +=1
print(sum) # Write the print statement outside the loop