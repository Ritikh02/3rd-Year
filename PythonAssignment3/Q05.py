# Question 5: Write a function that takes a positive integer and returns the number of digits.

def count_digits(number):
    return len(str(number))

user_number = int(input("Enter a positive integer: "))
print(count_digits(user_number))
