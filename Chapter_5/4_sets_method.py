# There are various methods in set

# Properties of set

# It is unordered
# It is unindexable
# There is no way to change an item in sets
# Sets cannot contain duplicate values

value = {1,3,78,78,3,3,3,3,3}
value.add(0) # It adds an value in the set -->{0, 1, 3, 78}
value.remove(0) # It instantly removes the specified value from the set --> {1, 3, 78}
value.pop() # It removes an random element from the set which is not good enough to be used 
value.clear() # It's going to empty the whole set 

S1 = {1,2,3,4,5}
S2 = {2,5,1,6}
print(S1.union(S2)) # It will follow the not repeatable and even give the return of both the set --> {1, 2, 3, 4, 5, 6}
print(S1.intersection(S2)) # It will return the common value of the two sets --> {1, 2, 5}

print(value,type(value))