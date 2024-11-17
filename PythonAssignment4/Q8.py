# 8. Write a function that takes n as an input and creates a list of n lists such that ith list contains the first five multiples of i.

n = int(input("Enter n: "))
result = [[i * j for j in range(1, 6)] for i in range(1, n + 1)]
print("Result:", result)
