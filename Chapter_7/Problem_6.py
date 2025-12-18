# Find the factorial of the given number using for loop

n = int(input("Enter your number to find factorail : "))
product = 1
for i in range(1,n+1):   # for the range function it takes around 1 to the before value of n like "1 to 5" it will take "1 to 4"
    product = product * i  #
    
    
print(f"The factorial of {n} = {product}")

'''Basically the value continues like 1*2=2 2 is stored in product then i increses so it goes 2*3 =6
its simple '''
# | Step | i | product (before) | Operation | product (after) |
# | ---- | - | ---------------- | --------- | --------------- |
# | 1    | 1 | 1                | 1 × 1     | 1               |
# | 2    | 2 | 1                | 1 × 2     | 2               |
# | 3    | 3 | 2                | 2 × 3     | 6               |
# | 4    | 4 | 6                | 6 × 4     | 24              |
# | 5    | 5 | 24               | 24 × 5    | 120             |

