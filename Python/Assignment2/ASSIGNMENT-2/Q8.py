# Write a program that takes an integer input from the user and continuously prompts until a positive number. If the final number is even, multiply by 2; if odd, square it.


num = int(input("Enter an integer: "))

while num <= 0:
    num = int(input("Please enter a positive number: "))

if num % 2 == 0:
    result = num * 2
else:
    result = num ** 2

print(f"Result: {result}")
