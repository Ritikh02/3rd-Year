# Write a program that finds the sum of the n terms of the series: 1 − x²/2! + x⁴/4! − x⁶/6! + . . . + x²n/(2n)!

from math import factorial

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms n: "))
series_sum = 0

for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i)) / (factorial(2 * i))
    series_sum += term

print(f"The sum of the series is: {series_sum}")
