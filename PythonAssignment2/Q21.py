# Write a python program to determine whether or not a number n is a factorial number.


n = int(input("Enter a number: "))
factorial_value = 1
i = 1

while factorial_value < n:
    i += 1
    factorial_value *= i

if factorial_value == n:
    print(f"{n} is a factorial number.")
else:
    print(f"{n} is not a factorial number.")
