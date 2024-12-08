# 9. Write a program to find the number of occurrences of each letter present in a given string., e.g.,
# str='mississippi' ⇒ {'m': 1, 'i': 4, 's': 4, 'p': 2}

string = "mississippi"
letter_counts = {letter: string.count(letter) for letter in set(string)}
print(letter_counts)