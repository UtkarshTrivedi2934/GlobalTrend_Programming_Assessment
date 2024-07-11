# -*- coding: utf-8 -*-
"""GlobalTrend_Programming_Assessment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u64kJl_N7Fsqu1VSvABCKHv74QntIMKn

# **Global Trend Programming Profile Assessment Questions**

1. **Implement a Python class MaxHeap that supports the following operations: insert, delete, and get_max. Ensure the operations maintain the properties of a max-heap.**
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            raise IndexError("delete from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def get_max(self):
        if len(self.heap) == 0:
            raise IndexError("get from an empty heap")
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def __str__(self):
        return str(self.heap)

# Example usage:
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(7)
heap.insert(30)

print(heap)        # Output: [30, 10, 20, 5, 7]
print(heap.get_max())  # Output: 30

heap.delete()      # Removes the maximum element (30)
print(heap)        # Output: [20, 10, 7, 5]

"""2. **Write a Python function that takes a list of URLs, attempts to download their content, and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions.**"""

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

def download_content(urls):
    contents = {}
    for url in urls:
        attempts = 0
        success = False
        while attempts < 3 and not success:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                contents[url] = response.text
                success = True
            except HTTPError as http_err:
                print(f"HTTP error occurred: {http_err} - URL: {url}")
            except ConnectionError as conn_err:
                print(f"Connection error occurred: {conn_err} - URL: {url}")
            except Timeout as timeout_err:
                print(f"Timeout error occurred: {timeout_err} - URL: {url}")
            except RequestException as req_err:
                print(f"Error occurred: {req_err} - URL: {url}")
            finally:
                attempts += 1
                if not success and attempts < 3:
                    print(f"Retrying {url} (attempt {attempts + 1})...")

        if not success:
            contents[url] = None
            print(f"Failed to retrieve {url} after 3 attempts")

    return contents

# Example usage:
urls = [
    "https://www.example.com",
    "https://www.nonexistentwebsite.com",  # This will fail
    "https://www.google.com"
]

result = download_content(urls)
for url, content in result.items():
    if content:
        print(f"Content from {url[:30]}...: {content[:100]}")  # Print first 100 characters of the content
    else:
        print(f"No content retrieved from {url}")

"""3. **Write a Python script that trains a simple linear regression model using scikit-learn. Use a dataset of your choice, split it into training and testing sets, and evaluate the model's performance.**"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler

# Load the diabetes dataset
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.Series(diabetes.target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the numerical columns
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

# Evaluate the model
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("Training set evaluation:")
print(f"Mean Squared Error: {train_mse:.2f}")
print(f"R^2 Score: {train_r2:.2f}")

print("\nTesting set evaluation:")
print(f"Mean Squared Error: {test_mse:.2f}")
print(f"R^2 Score: {test_r2:.2f}")

# Display model coefficients
print("\nModel coefficients:")
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)

"""4. **Using pandas, write a Python function to clean and preprocess a given DataFrame, which involves handling missing values, normalizing numerical columns, and encoding categorical columns.**"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def preprocess_data(df):
    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Preprocessing for numerical data: Impute missing values and normalize
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Preprocessing for categorical data: Impute missing values and one-hot encode
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine transformations using ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    # Apply transformations
    df_processed = preprocessor.fit_transform(df)

    # Get the feature names after encoding
    num_features = numerical_cols
    cat_features = preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols)
    feature_names = list(num_features) + list(cat_features)

    # Convert to DataFrame
    df_processed = pd.DataFrame(df_processed, columns=feature_names)

    return df_processed

# Example usage:
data = {
    'age': [25, 30, 35, 40, None],
    'income': [50000, 60000, 70000, 80000, 90000],
    'gender': ['male', 'female', None, 'female', 'male'],
    'city': ['New York', 'Los Angeles', 'Chicago', None, 'New York']
}

df = pd.DataFrame(data)
cleaned_df = preprocess_data(df)
print(cleaned_df)

"""5. **Write a Python function to compute the nth Fibonacci number using recursion.**"""

def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

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

"""7. **Write a Python decorator that measures the execution time of a function and logs it. Apply this decorator to a function that performs a computationally expensive task.**

"""

import time
import functools

def measure_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

# Example: Function that performs a computationally expensive task
@measure_execution_time
def compute_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example usage:
number = 1000
result = compute_factorial(number)
print(f"{number}! = {result}")

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

"""9. **Write a Python function that generates a random password. The password should contain a mix of uppercase letters, lowercase letters, digits, and special characters.**

"""

import random
import string

def generate_random_password(length=12):
    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example usage:
random_password = generate_random_password()
print(f"Generated Random Password: {random_password}")

"""10. **Write a Python function that takes a 2D list (matrix) and returns its transpose.**"""

def transpose_matrix(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix to store the transpose
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    # Fill the transpose matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(matrix)
for row in transposed:
    print(row)

"""***CODE BY UTKARSH TRIVEDI***"""