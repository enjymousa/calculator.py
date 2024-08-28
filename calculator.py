def perform_operation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
    elif operation == "^":
        return num1 ** num2
    else:
        print("Invalid operation")
def calculator():
    first_number = float(input("Number 1: "))

    while True:
        operation = input("Choose an operation (+, -, *, /, ^) or type 'stop' to quit: ")
        
        if operation.lower() == 'stop':
            print("calculator stopped.")
            break
        
        second_number = float(input("Number 2: "))

        new_result = perform_operation(first_number, second_number, operation)
        
        if new_result is not None:
            first_number = new_result
            print(f"The result is: {first_number}")

calculator()
