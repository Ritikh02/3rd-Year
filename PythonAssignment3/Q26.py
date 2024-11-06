# Question 26: Write a function that replaces all vowels in a string with the character ”*”.

def replace_vowels(input_string):
    return ''.join('*' if char in "aeiouAEIOU" else char for char in input_string)

user_input = input("Enter a string: ")
print(replace_vowels(user_input))
