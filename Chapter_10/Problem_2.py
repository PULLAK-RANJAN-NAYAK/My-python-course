# Create a class Calculator capable of finding square,cube and squareroot of a number

class calculator():
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The square is {self.n*self.n}")
        
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
        
    def sqrt(self):
        sqrt = self.n ** 0.5
        print(f"The square root is {sqrt:.2f}")
    
A = calculator(int(input("Enter a number : ")))
A.square()
A.cube()
A.sqrt()