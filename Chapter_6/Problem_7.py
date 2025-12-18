# Check wheather the person is talking about ranjan 

comment = input("Enter your comment : ")

if("Ranjan".lower() in comment.lower()):  # .lower() will convert the letters in lower 
    print("They are talking about ranjan") # if someone wrote "RaNJaN then also it will detect"
else:
    print("Anyone else")