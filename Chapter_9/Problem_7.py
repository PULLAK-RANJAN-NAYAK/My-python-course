# See on which line python is present in a log file

with open("log.txt") as f:
    lines = f.readlines()
    
    lineno = 1
    for line in lines:
        if("python" in line):
            print("Yes python in file")
            break
    else:
        print("Python is not present ")