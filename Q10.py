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