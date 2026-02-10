try:
    a = int(input("Enter a number : "))  # Take integer input
    print(a)

except Exception as e:
    print(e)  # Print error message

else:  # Runs only if try block executes without error
    print("Thank you")
