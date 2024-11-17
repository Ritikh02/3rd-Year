# 18. Write a Python program to create a new list that contains the square of every element in a given list using list comprehension.

lst = list(map(int, input("Enter list elements: ").split()))
squared = [x ** 2 for x in lst]
print("Squared list:", squared)
