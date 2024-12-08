# Create a program that determines and displays the number of unique characters in a string entered by the user, 
# e.g., Hello, World! has 10 unique characters, while zzz has only one unique character. 
# Use a dictionary or set to solve this problem.

user_string = input("Enter a string: ")
unique_characters = set(user_string)
print(f"The number of unique characters in the string is: {len(unique_characters)}")
