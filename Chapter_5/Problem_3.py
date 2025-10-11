# Can we have 18(int) and 18(string) in a set

s = set()

s.add(18)
s.add("18")

print(s)

# Output : 
#     {18, '18'}