# Question 6: Define a function to check if a given string is a palindrome. Example: madam ⟲ madam, racecar ⟲ racecar.

def is_palindrome(input_string):
    return input_string == input_string[::-1]

user_input = input("Enter a string: ")
print(is_palindrome(user_input))
