# Question 27: Write a function that takes a positive number as an input and converts the respective digits into corresponding text. Example: 85 → eight five, 123 → one two three.

def digits_to_text(number):
    digit_text = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return ' '.join(digit_text[int(digit)] for digit in str(number))

user_number = int(input("Enter a positive number: "))
print(digits_to_text(user_number))
