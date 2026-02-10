a = int(input("Enter a number : "))   # First number
b = int(input("Enter a number : "))   # Second number

if b == 0:
    # Manually raise error for division by zero
    raise ZeroDivisionError("Cannot divide numbers by zero (0)")
else:
    # Print division result with 2 decimal places
    print(f"The division of {a} and {b} is {a/b:.2f}")
