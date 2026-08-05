while True:
    try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if num2 == 0 and operation == "/":
                print("Cannot divide by zero. Try again")
                continue

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else: 
                print("Invalid number/or operation. Try again")
                continue

            rounded_result = round(result, 2)
            print("Result:", num1, operation, num2, "=", rounded_result)

            question = (input("Do you want to do a new operation? Y/N: "))
            if question == "Y":
                continue
            elif question == "N":
                print("Goodbye!")
                break

    except ValueError:
        print("Invalid number/or operation. Try again")
        