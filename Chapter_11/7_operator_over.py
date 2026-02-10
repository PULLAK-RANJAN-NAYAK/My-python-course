# Operator overloading using a class

class Operator:
    def __init__(self, n):
        self.n = n   # Store value in object

    def __add__(self, num):
        return self.n + num.n

    def __sub__(self, num):
        return self.n - num.n

    def __mul__(self, num):
        return self.n * num.n

    def __truediv__(self, num):
        return self.n / num.n

    def __floordiv__(self, num):
        return self.n // num.n


# Taking user input
n = int(input("Enter the value of n : "))
m = int(input("Enter the value of m : "))

# Creating objects
a = Operator(n)
b = Operator(m)

# Performing all operations using a loop
operations = [
    ("Addition", a + b),
    ("Subtraction", a - b),
    ("Multiplication", a * b),
    ("Division", a / b),
    ("Floor Division", a // b)
]

# Displaying results
for op, result in operations:
    print(op, ":", result)


# Python does not know how operators work for user-defined classes,
# so special methods like __add__, __sub__, __mul__ are used to define them.
