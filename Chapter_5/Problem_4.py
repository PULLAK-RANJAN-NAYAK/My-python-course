# What will be the length of the set

s = set()

s.add(20)
s.add(20.0)
s.add("20")

print(len(s)) # The output is 3 as there are 3 values in the set 
print(s) # This is without len function --> {'20', 20}
# Even when the float and the integer value is same the length of the set is --> 2(output
# )
# >>> 1==1.00
# True    # If the  interger value is equal to the float value then the value in the set will be 2