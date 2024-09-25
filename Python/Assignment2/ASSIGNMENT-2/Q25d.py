# Question 4: Print a diamond pattern of asterisks.
for i in range(4):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

for i in range(3, -1, -1):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()