# using global variable inside a function

a = 89

def fun():
    global a   # It will change the global value of a 
    a = 4
    print(a)

fun() 
print(a)   # If you write this before the function call it will show 89 then 4