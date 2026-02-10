# WAP to make a copy of the txt file

with open("this.txt") as f:   # open's the file 
    content = f.read()        
    
with open("this_copy.txt","w") as f:   # This will make and open a new file and copy 
    f.write(content)                           #the content in the new file