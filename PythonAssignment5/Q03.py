# Q3.  Write a program to take a user-input dictionary and print the sum of the values.

user_dict = {}

n = int(input("Enter the number of key-value pairs: "))
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    user_dict[key] = value

value_sum = sum(user_dict.values())
print("The sum of the values is:", value_sum)
