class InvalidOperationError(Exception):
    pass


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise InvalidOperationError("Unsupported operator.")


while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()

        result = calculate(num1, num2, operation)

        print("Result:", result)

    except ValueError:
        print("Invalid numeric input. Please enter valid numbers.")

    except ZeroDivisionError as error:
        print(error)

    except InvalidOperationError as error:
        print(error)

    finally:
        print("Calculation attempt completed.")

    retry = input("Do you want to try again? (yes/no): ").strip().lower()

    if retry != "yes":
        print("Calculator closed.")
        break