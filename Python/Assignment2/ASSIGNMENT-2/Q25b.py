# Question 2: Print a right-angled triangle of asterisks with decreasing height.
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()