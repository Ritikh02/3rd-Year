# Question 10: Create a function that returns all the unique permutations of a given string.

from itertools import permutations

def unique_permutations(input_string):
    return [''.join(p) for p in set(permutations(input_string))]

user_input = input("Enter a string: ")
print(unique_permutations(user_input))
