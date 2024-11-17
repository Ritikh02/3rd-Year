# 16. Write a Python program that prompts the user to enter a list and displays whether the list is sorted or not.
# Here is a sample run:
# Enter list: 8 10 15 16 16 19 11
# The list is not sorted

lst = list(map(int, input("Enter list elements: ").split()))
is_sorted = lst == sorted(lst)
print("The list is already sorted" if is_sorted else "The list is not sorted")
