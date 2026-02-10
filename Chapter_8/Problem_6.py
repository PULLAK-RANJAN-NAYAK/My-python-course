# WAP to convert inch to centimeters 

def inch_to_cen(inch):
    if(inch==0):
        return
    return inch * 2.54

inch = float(input("Enter value in inch : "))
print(f"In centimetes it is : {inch_to_cen(inch)}")