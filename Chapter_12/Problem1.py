# Write a program to open three files 1.txt, 2.txt, and 3.txt. 
# If any of these files are not present a message must be printed without exiting the program

try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)



# files = ["f1.txt", "f2.txt", "f3.txt"]

# for file in files:
#     try:
#         with open(file) as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"{file} not found")

# This is the shorter version
