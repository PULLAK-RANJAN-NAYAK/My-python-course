# Detect the key phrases "Make a lot of money", " buy now", "subscribe this " , "click this"

p1 = "Make a lot of money"
p2 = "buy now" 
p3 = "subscribe this " 
p4 = "click this"

comment = input("Enter you comment : ")

if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)): 
    print("This is a spam comment!!!") # The "in" function will check the phrase in the variable and confirms that it matches
else:
    print("This is not an spam   :)")