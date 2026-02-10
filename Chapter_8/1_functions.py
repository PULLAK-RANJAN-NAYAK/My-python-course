# A function is a group of statements performing a specific task

def average():
    a = int(input("Enter your number : "))
    b = int(input("Enter your number : "))
    c = int(input("Enter your number : "))
    
    avg = (a+b+c)/3
    print(avg)
    
for i in range(1,5):
    average()

