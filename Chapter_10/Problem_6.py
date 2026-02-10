# Can you change the self parameter to anything else

# Create a class to book train ticket,get status and get fare information of train running under 
# Indian railways

import random

class Train:
    def __init__(slf,trainno):  # As you can see nothing happens but you have to change the other self to slf
        slf.trainno = trainno    # Nothing will happen but it is not a good practise in programming 
        
    def book(self,fro,to): 
        print(f"Your ticket is booked in {self.trainno} from {fro} to {to}")
    
    def getstatus(self):
        print(f"Trainno:{self.trainno} is on time")
        
    def fareinfo(self,fro,to):
        print(f"Your fare in Trainno {self.trainno} from {fro} to {to} is {random.randint(500, 700)}")
        
    @staticmethod
    def message():
        print("This train is running under Indian railways")
        
Run = Train(12714)
Run.book("HYD","BHU")
Run.getstatus()
Run.fareinfo("HYD","BHU")
Run.message()
