"""6. **Write a Python function that divides two numbers and handles the case where the divisor is zero by returning a custom error message.**"""

def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result

# Example usage:
print(divide_numbers(10, 2))   # Output: 5.0
print(divide_numbers(5, 0))    # Output: Error: Division by zero is not allowed.
