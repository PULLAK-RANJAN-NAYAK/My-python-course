# A simple number guessing game

import random

n = random.randint(1,100)
a = -1
guesses = 1 

while(a !=n ):
    a = int(input("Enter the number : "))
    
    if(a > n):
        print("Lower number please","\n")
    elif(a < n):
        print("Higher number please","\n")
    guesses += 1
        
print(f"You have guessed the number {n} correctly in {guesses} attempts")