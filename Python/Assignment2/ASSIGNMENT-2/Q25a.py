# Question 1: Print a right-angled triangle of asterisks with increasing height.
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()