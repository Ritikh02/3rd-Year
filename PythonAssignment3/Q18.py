# Question 18: Write a function to check if a string is an Anagram of another string. (An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once, e.g. tom marvolo riddle ⇝ i am lord voldemort)

def is_anagram(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print(is_anagram(string1, string2))
