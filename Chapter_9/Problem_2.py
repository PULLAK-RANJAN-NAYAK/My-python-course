# Let a user play a game and return the score as an integer and read the hiscore.txt
#which is either blank or contains the previous hi-score of the player 
# WAP to update the hi-score whenever the game() breaks the hi-score

import random 

def game():
    print("You are playing a game ..")
    score = random.randint(1, 60)
    
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"Your score : {score}")
    
    if (score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
        return score
    
game()