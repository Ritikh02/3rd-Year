# 11. Write a Python program to print an M-by-N list in a tabular format.

M, N = map(int, input("Enter M and N: ").split())
matrix = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(N)] for i in range(M)]
for row in matrix:
    print(" ".join(map(str, row)))
