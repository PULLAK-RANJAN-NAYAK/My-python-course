# There are various ruled to sort and make changes to an list

list = ["crazy","ranjan",56,34.5678,True,False]
print(list)

list.append(True) # So append means adding an element at the last of an list
print(list)

list1 = [3,5,7,9,1,4,2,8,6]
list1.sort()
print(list1) # So sort will sort the elements in ascending order by default

list2 = [3,5,7,9,1,4,2,8,6]
list2.reverse()
print(list2) # So reverse will reverse the order of elements in the list

list3 = [3,5,7,9,1,4,2,8,6]
list3.insert(2,10) # index position , value to be inserted at the postition   (I:V)
print(list3) # So insert will insert the element at the given index and shift the rest of the elements to the right

list4 = [3,5,7,9,1,4,2,8,6]
list4.pop(4) # So pop will remove the element at the given index and return its value
print(list.pop(4)) #If you use this statement the pop function will return the value of the element that was removed at the given index
print(list4)

list5 = [3,5,7,9,1,4,2,8,6]
list5.remove(4) # So remove will remove the certain value from the list
print(list5)

list6 = [3,5,7,9,1,4,2,8,6]
list6.clear() # So clear will remove all the elements from the list
print(list6)



