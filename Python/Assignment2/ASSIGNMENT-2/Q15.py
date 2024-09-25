# Write a program to determine whether a given natural number is a perfect number.


num = int(input("Enter a natural number: "))
divisors_sum = sum(i for i in range(1, num) if num % i == 0)

if divisors_sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
