# Question 10: Print a pattern of alphabets in a triangular shape.
n = 65
for i in range(6):
    for j in range(i + 1):
        ch = chr(n)
        print(ch, end=" ")
        n += 1
    print()