# Write a program that finds the sum of the n terms of the series: 1 + x/1! + x²/2! + x³/3! + . . . + xⁿ/n!

from math import factorial

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms n: "))
series_sum = 0

for i in range(n + 1):
    term = (x ** i) / factorial(i)
    series_sum += term

print(f"The sum of the series is: {series_sum}")
