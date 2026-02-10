# The walrus operator allows you to assign values to a variable as part of an expression

if(n := len([1,2,3,4,5,6])) > 4:
    print("The list is too long , it should be <=4")
    
# Walrus types are used to identify the input type of a variable