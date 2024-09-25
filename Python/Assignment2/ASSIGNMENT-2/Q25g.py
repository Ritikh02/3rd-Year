# Question 7: Print a repeating numerical pattern with increasing repetition.
for i in range(1, 10, 2):
    for j in range(i):
        print(i, end="")
    print()