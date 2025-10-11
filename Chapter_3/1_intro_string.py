# # A string in python is immutable means if once made cannot be changed 

# name = "Pullak" # as you have made an string you cannot even change an single character in the string 
# index = name[4] # INDEX CONCEPT 
# print(index) # ONCE RUN AND YOU WILL UNDERSTAND 


# A small example test with try on's
A = input("enter a word : ")
x = A
b = int(input("Enter the index number : "))  
index = A[b]

print("The letter in the index is : ",index)

length = len(A)
print("The lenght of the word is : ",length)

Slicing = A[0:4]                             # Using this to get to slices value from the word
print("The sliced word is : ",Slicing)

#      Output
# enter a word : Thala
# Enter the index number : 3
# The letter in the index is :  l
# The lenght of the word is :  5         This is straight from terminal
# The sliced word is :  Thal
