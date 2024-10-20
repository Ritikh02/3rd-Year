# Question 14: Print a pattern 
a = 65
for i in range (1,8):
    for j in range(i):
        print(chr(a), end=" ")
        a += 1
    print()