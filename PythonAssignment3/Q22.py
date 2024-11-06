# Question 22: Create a function that prints the first 10 terms of an arithmetic progression.

def arithmetic_progression(first_term, common_difference):
    return [first_term + i * common_difference for i in range(10)]

first_term = int(input("Enter the first term: "))
common_difference = int(input("Enter the common difference: "))
print(arithmetic_progression(first_term, common_difference))
