# Question 23: Write a function that returns the index of each vowel in a string using a for loop.

def vowel_indices(input_string):
    return [i for i, char in enumerate(input_string) if char in "aeiouAEIOU"]

user_input = input("Enter a string: ")
print(vowel_indices(user_input))
