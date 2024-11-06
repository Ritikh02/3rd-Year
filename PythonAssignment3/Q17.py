# Question 17: Create a function that takes a string and returns a new string where all the vowels are removed.

def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)

user_input = input("Enter a string: ")
print(remove_vowels(user_input))
