# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter a number : "))

table = [f"{n} x {i} = {n*i}" for i in range(1, 11)]

with open("Tables.txt", "a") as f:
    for line in table:
        f.write(line + "\n")
