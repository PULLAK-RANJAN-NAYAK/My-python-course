#Write a program to convert celcius to fahrenheit using functions
 
def c_to_f(f):
    return 5*(f-32)/9 # Formula for fahrenheit to celsius 

f = int(input("Enter fahrenheit value : "))
c = c_to_f(f) #Store the function in the variable
print(f"In celcius is : {round(c,2)}°") #Round is used to round the value upto 2 integers after decimal