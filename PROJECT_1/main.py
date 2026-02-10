# WAP to make snake,water,gun game and play with the computer 

import random       

computer = random.choice([0,-1,1])  #With random module computer can choose randomly
youstr = input("Enter your choice : ").lower()  #Your input

youdict = {"snake":1,"water":-1,"gun":0}   #A dictionary to store the value
revdict = {1:"snake",-1:"water",0:"gun"}   #Reverse dictionary to show what to choose 

you = youdict[youstr]  #Storing your entered value and checking within the dictioanary 

print(f"You choose {revdict[you]}\nComputer choose {revdict[computer]}")

if(computer == you):  # If the randomly computer generates same number as you it's draw
    print("It's a draw")
elif(computer==0 and you==-1)or\
    (computer==-1 and you==1)or\
    (computer==1 and you==0):         #Checking the conditions if its true
        print("You win")
else:
    print("You lose")

# Well this was a simple game 

# Hope it brings some memory back playing hand to hand and while it on this date 
