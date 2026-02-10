# See whether python is present in a log file

with open("log.txt","r") as f:
    content = f.read()

if("python" in content):
    print("Yes python in file")
else:
    print("Python is not present ")