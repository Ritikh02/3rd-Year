# Question 24: Write a function that removes all punctuation from a string.

import string

def remove_punctuation(input_string):
    return ''.join(char for char in input_string if char not in string.punctuation)

user_input = input("Enter a string: ")
print(remove_punctuation(user_input))
