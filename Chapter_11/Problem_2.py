# Create a class pets from class animal and further create a class dog and add a method bark

class Animals:
    pass

class pets(Animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("bow bow")
        
d = dog()

d.bark()
        
        