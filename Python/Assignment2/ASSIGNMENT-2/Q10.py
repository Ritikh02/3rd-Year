# Write a program that takes a string as input and prints all possible substrings of the string


string = input("Enter a string: ")

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        print(string[i:j])
