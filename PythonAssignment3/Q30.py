# Question 30: Write a function that inputs a number and returns the product of digits of that number.

def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

user_number = int(input("Enter a number: "))
print(product_of_digits(user_number))
