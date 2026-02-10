# Greet the person whose name starts with S

list = ["Ranjan","Soham","Swastik","Pullak","Swati"]

for name in list:
    if(name.startswith("S")):
        print(f"Hello {name}") 
        
        
        
list = ["Ranjan","Soham","Swastik","Pullak","Swati"]

for name in list:
    if(name.lower().startswith("s")): # You can even do the chaining like name.lower().startswith("S")
        print(f"Hello {name}") # the lower() will help to convert the whole name smaller so it doesn't miss