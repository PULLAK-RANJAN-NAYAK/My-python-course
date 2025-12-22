# This is an simple calculator type project that I will be doing the addition,substraction,division,multiplication
#Features showing the history,performing operations
#Pure Python based project

operations = {
    "+" : "Addition",
    "-" : "Substarction",
    "*" : "Multiplication",
    "/" : "Division"
}

history = []

result = float(input("Enter initial number: "))

while True:
    print("Available operations")
    for op in operations :
        print(op ,"-",operations[op])
    
    operator = input("Enter operator(+,-,*,/) or = to exit : ")

    if operator == "=":
        print(f"Final result : {result}")
        break
    if operator not in operations: 
        print(f"\nInvalid Input : {operator}")
        continue

    num = float(input("Enter next number : "))

    if operator == "+":
        new_result = result + num
    elif operator == "-":
        new_result = result - num
    elif operator == "*":
        new_result = result * num
    elif operator == "/":
        if num == 0:
            print("Cannot divide by zero(0)!")
            continue
        new_result = result / num

    history.append(f"{result} {operator} {num} = {new_result}")
    result = new_result

    print("Current result:", result)

#History
print("\nCalculation history : ")
for step in history:
    print(step)

        