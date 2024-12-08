# 12. Write a program that uses a dictionary to determine and print the number of duplicate words in a sentence. 
# Treat uppercase and lowercase letters the same and assume there is no punctuation in the sentence.

sentence = "This is a test This test is a test"
words = sentence.lower().split()
word_count = {word: words.count(word) for word in set(words)}
duplicates = {word: count for word, count in word_count.items() if count > 1}
print(duplicates)