# 12. Define a function that returns the sum of all the elements in a specified column in a matrix. 
# Write a Python program that reads a 3-by-4 matrix and displays the sum of each column.

matrix = [list(map(float, input("Enter row: ").split())) for _ in range(3)]
column_sums = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
print("Column sums:", column_sums)
