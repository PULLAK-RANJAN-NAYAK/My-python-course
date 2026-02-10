# Use rthe class 2-D and use it to create another class representing a 3-D vector

class Twovector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2-D vector is {self.i}i + {self.j}j")
    
class Threevector(Twovector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
            
    def show(self):
        print(f"The 3-D vector is {self.i}i + {self.j}j + {self.k}k ")
        
a = Twovector(1,2)
b = Threevector(1,2,3)

a.show()
b.show()