# Add a static method in question 2 to greet the user 

# Create a class Calculator capable of finding square,cube and squareroot of a number

class calculator():
    def __init__(self,n):
        self.n = n
        print("The solution of your number are : ")
    
    def square(self):
        print(f"The square is {self.n*self.n}")
        
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
        
    def sqrt(self):
        sqrt = self.n ** 0.5
        print(f"The square root is {sqrt:.2f}")
        
    @staticmethod  # This is used as we don't want to use self 
    def hello():
        print("Hello User")
    
A = calculator(int(input("Enter a number : ")))
A.square()
A.cube()
A.sqrt()
A.hello()