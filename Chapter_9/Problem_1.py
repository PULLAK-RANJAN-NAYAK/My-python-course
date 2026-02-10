# Find whether the word twinkle is present in the given file poem.txt

f = open("poem.txt")
content = f.read()

if("Twinkle" in content):
    print("Twinkle present in the file")
else:
    print("Twinkle not present in the file")
    
f.close()