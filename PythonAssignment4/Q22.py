# 26. When combining filter and map operations, the order in which they’re performed matters.
# Consider a list numbers containing 10, 3, 7, 1, 9, 4, 2, 8, 5, 6 and the following code:
# In [1]: numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
# In [2]: list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
# Out[3]: [20, 8, 4, 16, 12]
# Reorder this code to call map first and filter second. What happens and why?

# The list of numbers
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

# Original Code: filter first, then map
original_result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))

# Reversed Code: map first, then filter
reversed_result = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))

# Explanation:
# 1. In the original code (filter first, then map), the filter operation first selects even numbers from the list [10, 4, 2, 8, 6],
#    and then the map operation doubles each of them to get the result [20, 8, 4, 16, 12].
# 2. In the reversed code (map first, then filter), the map operation first doubles all the numbers in the list [20, 6, 14, 2, 18, 8, 4, 16, 10, 12],
#    and then the filter operation selects only the even numbers from the transformed list, which results in [20, 6, 14, 2, 18, 8, 4, 16, 10, 12].

# Print the results
print("Original Result (filter first, map second):", original_result)
print("Reversed Result (map first, filter second):", reversed_result)
