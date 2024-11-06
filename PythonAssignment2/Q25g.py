# Question 7: Print a pattern
n = 5
for i in range(1, n):
    print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + ('*' if i > 1 else ''))
print('*' * (2 * n - 1))



