# A program to print star pattern using for loop
'''
  *
 ***
*****
'''

n = int(input("Enter the number of rows : "))

for i in range(1,n+1):
    print(" "* (n-i),end = "") # The end fuction is used so that the print statement doesn't give a new line 
    print("*"* (2*i-1), end = "\n")
    
'''The output without the end statement in the print statement is
*

***

*****            see that it is annoying 

*******

*********
'''


'''This one is the easy one as 
The space is printed as per the row like n = 5 then space will be n-i hence i is the range and is increased by the range
and the star's are printed like 2*i-1 to adjust with the space 
Just remember and figure out the logic behind it 
'''