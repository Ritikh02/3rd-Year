# 10. Write a program to find the number of occurrences of each vowel present in a given string, and also
# print the vowels.

string = "mississippi"
vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_counts = {vowel: string.count(vowel) for vowel in vowels if vowel in string}
print(vowel_counts)