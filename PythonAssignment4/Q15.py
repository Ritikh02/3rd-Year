# 15. Write a Python program that randomly fills in 0s and 1s into a 4-by-4 matrix, prints the matrix, 
# and finds the first row and column with the most 1s.

import random

matrix = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]
print("Matrix:")
for row in matrix:
    print(row)

row_max = max(range(4), key=lambda i: sum(matrix[i]))
col_max = max(range(4), key=lambda i: sum(row[i] for row in matrix))

print("Row with most 1s:", row_max)
print("Column with most 1s:", col_max)
