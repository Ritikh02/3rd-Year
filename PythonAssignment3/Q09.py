# Write a Python function to find the first, second and third greatest digit in a number.

def find_top_three_digits(number):
    digits = sorted(set(str(number)), reverse=True)
    if len(digits) < 3:
        return "The number must contain at least three unique digits."
    first = digits[0]
    second = digits[1]
    third = digits[2]
    return f"The top three greatest digits are: {first}, {second}, and {third}"

user_number = input("Enter a number: ")
print(find_top_three_digits(user_number))
