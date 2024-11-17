# 17. You can compute the standard deviation with the following formula; you have to store the individual numbers using a list so that they can be used after the mean is obtained.
# mean = (x1 + x2 + x3 + ... + xn) / n
# deviation = sqrt((sum(xi - mean)^2) / (n - 1))

import math

numbers = list(map(float, input("Enter 10 numbers: ").split()))
mean = sum(numbers) / len(numbers)
std_dev = math.sqrt(sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1))

print("Mean:", mean)
print("Standard Deviation:", std_dev)
