# 19. Given a long list of words, write a Python function unique_pairs(words) to find all unique pairs of words that:
# • Have no common letters.
# • Each word in the pair should have at least 4 letters.
# • Each unique pair should be stored in a set as a tuple in lexicographical order.

def unique_pairs(words):
    words = [word for word in words if len(word) >= 4]
    result = set()
    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if not set(words[i]) & set(words[j]):
                result.add(tuple(sorted((words[i], words[j]))))
    
    return result

# Example usage:
words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
print(unique_pairs(words))