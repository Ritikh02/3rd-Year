# Question 14: Write a function to determine if a given number is an Armstrong number. (An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the number of digits, e.g., 153 = 1^3 + 5^3 + 3^3, 1634 = 1^4 + 6^4 + 3^4 + 4^4).

def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    return number == sum(int(digit) ** power for digit in digits)

user_number = int(input("Enter a number: "))
print(is_armstrong(user_number))
