# Question 11: Create a function that determines whether a string can be rearranged to form a palindrome.

from collections import Counter

def can_form_palindrome(input_string):
    count = Counter(input_string)
    odd_count = sum(1 for val in count.values() if val % 2 != 0)
    return odd_count <= 1

user_input = input("Enter a string: ")
print(can_form_palindrome(user_input))
