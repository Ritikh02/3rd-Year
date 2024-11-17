# Input 10 integers from the keyboard into a list. The number to be searched is entered through the
# keyboard by the user. Write a Python program to find if the number to be searched is present in the
# list and if it is present, display the number of times it appears in the list.

lst = [int(input("Enter element: ")) for _ in range(10)]
search = int(input("Enter number to search: "))
count = lst.count(search)
print(f"Number {search} appears {count} times." if count > 0 else "Number not found.")
