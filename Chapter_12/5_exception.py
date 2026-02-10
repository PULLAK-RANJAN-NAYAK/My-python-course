try:
    # Take integer input
    a = int(input("Enter a number : "))
    print(a)

except Exception as e:
    # Print error if input is invalid but it doesn't crash the program 
    print(e)

# Always executes
print("Thank you")

# Output : 
# Enter a number : rerere
# invalid literal for int() with base 10: 'rerere'
# Thank you