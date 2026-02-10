# WAP to find whether both the files contents are identical and matches the content 
# another file

with open("this_copy.txt") as f:
    content = f.read()
    
with open("this.txt") as f:
    content1 = f.read()
    
if(content == content1):
    print("The contents in the files are same ")
else:
        print("The contents in the files are not same ")
    