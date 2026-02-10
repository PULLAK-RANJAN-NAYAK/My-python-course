# WAP to print the 3,5,7 element in the iist using the enumerate function

l1 = [1,2,3,4,5,6,7,8,9,0]

for index,item in enumerate(l1):
    if index == 2 or index == 4 or index == 6:
        print(item)