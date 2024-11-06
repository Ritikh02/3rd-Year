# Write a python program that displays all the numbers from 100 to 1,000, ten per line, that are divisible by 5 or 6.


count = 0
for num in range(100, 1001):
    if num % 5 == 0 or num % 6 == 0:
        print(num, end=' ')
        count += 1
        if count % 10 == 0:
            print()
