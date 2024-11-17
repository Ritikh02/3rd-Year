# Write a Python program that removes all occurrences of a specific element from a list.

lst = list(map(int, input("Enter list elements: ").split()))
element = int(input("Enter the element to remove: "))
lst = [x for x in lst if x != element]
print("Updated list:", lst)
