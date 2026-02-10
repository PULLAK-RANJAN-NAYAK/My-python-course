list = [3,513, 53,555]

# index = 0
# for item in list:
#     print(f"The number at index{index} is {item}")
#     index += 1 

# This can be simplified using enumerate function

for index,item in enumerate(list):
    print(f"the item number at index{index} in {item}")