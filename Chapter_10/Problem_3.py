# Create a class and set a attribute value and then create an object and try to change the attribute
# value and see whether the class attribute value is changed or not

class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because any instance was not present 
o.a = 0        # Instance attribute is present 
print(o.a)
print(Demo.a)   # Class attribute is printed as it is not changed 