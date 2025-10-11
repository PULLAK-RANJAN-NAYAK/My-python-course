# The double space you found in the problem 3 make it single space

# name = "Ranjan is  an  ambivert"
# print(name.find("  ").replace("  ", " "))  You can't use both function at same time as using find gives you an int
                                           #not an string so use both the function seperately 
                                           

name = "Ranjan is  an  ambivert"
print(name.replace("  "," "))  # There you go the answer -- Ranjan is an ambivert
print(name) # String are immutable as you cannot change them by running functions on them 

# Output : 
# Ranjan is an ambivert
# Ranjan is  an  ambivert