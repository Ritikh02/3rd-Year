# Question 10: Print a pattern 
n = 5
for i in range(n, -1, -1):
    for j in range(i+1):
        print(j, end=" ")
    print()
