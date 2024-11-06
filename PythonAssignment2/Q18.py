# Write a Python program that prints all numbers from 1 to 100, except multiples of 7, using a for loop with continue.


for num in range(1, 101):
    if num % 7 == 0:
        continue
    print(num, end=' ')
