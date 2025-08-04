while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Choose the operation:")
    print("1. +\n2. -\n3. *\n4. /\n5. %")
    operator = input("Enter the operation (+, -, *, /, %): ")

    if operator == "+":
        print("The answer is", a + b)
    elif operator == "-":
        print("The answer is", a - b)
    elif operator == "*":
        print("The answer is", a * b)
    elif operator == "/":
        if b != 0:
            print("The answer is", a / b)
        else:
            print("Error: Division by zero!")
    elif operator == "%":
        print("The answer is", a % b)
    else:
        print("Invalid operation")
    option = input("Press Enter to continue or type 'exit' to quit: ")
    if option.lower() == 'exit':
        print("Exiting the calculator.")
        break
