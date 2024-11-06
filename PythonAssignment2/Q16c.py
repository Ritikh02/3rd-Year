# Write a program that finds the sum of the series: 1-3+5-7+9-...

n = int(input("Enter the number of terms n: "))
series_sum = 0

for i in range(n):
    term = (-1) ** i * (2 * i + 1)
    series_sum += term

print(f"The sum of the series is: {series_sum}")
