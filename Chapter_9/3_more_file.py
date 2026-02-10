# There are more file function

f = open("file.txt")
lines = f.readlines() # This is going to read the lines in one go and store it into a list 

# You can go one line at a time also 

# line1 = f.readline()
# print((line1),type(line1))

# Output for the line1 is :
#     I am Ranjan
#     <class 'str'>

print(lines,type(lines))  # Type here will be list 
f.close()