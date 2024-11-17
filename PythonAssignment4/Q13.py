# 13. Write a Python function that sorts a list of tuples based on the second element of each tuple.

lst = [(1, 2), (3, 1), (5, 4)]
sorted_lst = sorted(lst, key=lambda x: x[1])
print("Sorted list:", sorted_lst)
