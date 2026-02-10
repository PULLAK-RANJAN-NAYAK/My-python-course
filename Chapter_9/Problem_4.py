# A file consists of donkey word multiple times so replace it with "####"

word = "Donkey"

with open("Donkey.txt","r") as f:
    content = f.read()

contentnew = content.replace(word,"####")

with open("Donkey.txt","w") as f:
    f.write(contentnew)