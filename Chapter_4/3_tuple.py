# So as list is mutable but tuple here is immutable

a = (1, 2, 3, 4, 5)
print(type(a)) # So tuple is a list of data types just as list but it is immutable
#If you want to create an tuple but with one element then put comma after the single element  (1,)--> tuple

b = (1)
print(type(b)) # As the output states the type of b is integer


# Output : 
# <class 'tuple'>
# <class 'int'>