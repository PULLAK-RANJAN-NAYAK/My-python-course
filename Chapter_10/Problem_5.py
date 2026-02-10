# Create a class to book train ticket,get status and get fare information of train running under 
# Indian railways

import random

class Train:
    def __init__(self,trainno):
        self.trainno = trainno
        
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
