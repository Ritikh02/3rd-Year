# 13. Write a function that receives a list of words, then determines and displays in alphabetical order only 
# the unique words. Treat uppercase and lowercase letters as the same. The function should use a set to 
# get the unique words in the list. Test your function with several sentences.

def unique_words_alphabetical(words):
    unique_words = set(word.lower() for word in words)
    return sorted(unique_words)

words_list = ["This", "is", "a", "test", "this", "Test", "is", "unique"]
print(unique_words_alphabetical(words_list))