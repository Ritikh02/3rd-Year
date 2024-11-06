# Question 28: Write a function that takes a string of lowercase alphabets as inputs and gives an output by shifting them by one letter ahead. Note that if the string has ’z’, then it will be treated as ’a’. Example: python → qzuipo, pythonzabc → qzuipobbcd.

def shift_letters(input_string):
    return ''.join(chr(((ord(char) - 97 + 1) % 26) + 97) if char.islower() else char for char in input_string)

user_input = input("Enter a string of lowercase alphabets: ")
print(shift_letters(user_input))
