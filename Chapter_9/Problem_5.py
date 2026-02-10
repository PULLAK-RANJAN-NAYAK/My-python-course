# Replace the list of words as you did in question 4 

words = ["Donkey".lower(),"Bad".lower(),"Potty".lower()]

with open("donkey1.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open("donkey1.txt","w") as f:
    f.write(content)