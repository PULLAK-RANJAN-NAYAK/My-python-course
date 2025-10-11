# Dictionary type data type so basicaly it is an type which can store both the variable and the value inside the variable
# To avtually know that it is a dictionary type simply the data stored in the variable is in {}(curly bracket)
# Simple putting it down it is an collection of the data 

# Properties if dictionary is 
# 1. It is unorderd
# 2. It is mutable
# 3. It is indexed
# 4. Cannot contain duplicate keys

marks = {
    "Ranjan":50,
    "Pullak":78,
    "Nayak":100
}

print(marks,type(marks))  #Output--> {'Ranjan': 50, 'Pullak': 78, 'Nayak': 100} <class 'dict'>
# print(marks[1]) # Error as there is no index in the dictionary

print(marks["Ranjan"]) # Rather than going with the index you can do this |||| Output-->50
