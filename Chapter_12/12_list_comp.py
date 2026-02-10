# A list comprehension is an elegant way to create lists based on the existing list 

l1 = [1,2,4,5,6,8]

# squarelist = []
# for item in l1:
#     squarelist.append(item*item)
# print(squarelist)


squarelist = [i*i for i in l1 ]
print(squarelist)