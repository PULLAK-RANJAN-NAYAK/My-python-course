# So basically with statement is used for the alternative of the f.close()

with open("file.txt") as f:
    print(f.read())

# You don't have close the file after it comes out of the with statement it closes 