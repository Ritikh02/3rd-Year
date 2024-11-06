# Question 7: Write a Python function to check whether an alphabet is a vowel or consonant.

def check_vowel_consonant(alphabet):
    vowels = "aeiouAEIOU"
    return "Vowel" if alphabet in vowels else "Consonant"

user_alphabet = input("Enter an alphabet: ")
print(check_vowel_consonant(user_alphabet))
