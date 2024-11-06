# Write a program that takes a number from the user and continuously sums its digits until the sum becomes a single-digit number.


num = input("Enter a number: ")

while len(num) > 1:
    digit_sum = sum(int(digit) for digit in num)
    num = str(digit_sum)

print(f"The single-digit sum is: {num}")
