# Now to show the type of the data stored in a variable

a = "ranjan"
b = type(a)
print(b)

c = "34.2"
d = float(c) #you can change an type of teh value using the type function
e = type(d)
print(e)
    
f = "Ranjan"
g = float(f) #as its going to show an error as you can't convert an string into float,integer or boolan
h = type(g) # you can convert string type to any data type until their is int or float inside double quotes
print(h) 