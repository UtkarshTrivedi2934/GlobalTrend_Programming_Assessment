"""8. **Write a Python function that takes two numbers and an operator (as a string) and performs the corresponding arithmetic operation (addition, subtraction, multiplication, or division).**"""

def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator. Use '+', '-', '*', or '/'.")

    return result

# Example usage:
try:
    num1 = 10
    num2 = 5
    operator = '+'
    result = arithmetic_operation(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

    operator = '*'
    result = arithmetic_operation(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

    num1 = 15
    num2 = 0
    operator = '/'
    result = arithmetic_operation(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

    num1 = 8
    num2 = 0
    operator = '/'  # This will raise a ValueError
    result = arithmetic_operation(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

except ValueError as ve:
    print(ve)
