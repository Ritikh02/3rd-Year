# Question 8: Print a pattern
n = 4
for i in range(1, n+1):
    print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + ('*' if i > 1 else ''))
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + ('*' if i > 1 else ''))
