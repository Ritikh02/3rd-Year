# Write a python program that accepts a positive integer n and reverses the order of its digits.


n = int(input("Enter a positive integer: "))
reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10

print(f"The reversed number is: {reversed_number}")
