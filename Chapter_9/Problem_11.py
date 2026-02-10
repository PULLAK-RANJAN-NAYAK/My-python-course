#WAP to rename the file 

with open("rename_old.txt") as f:
    content = f.read()
    
with open("rename_new","w") as f:
    f.write(" ")  