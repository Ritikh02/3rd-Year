# Question 9: Print a numerical pattern forming an inverted pyramid with 1 at the top.
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()