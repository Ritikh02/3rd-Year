# 10. Write a Python function that takes a tuple of tuples and prints the sum of all numeric elements in the inner tuples.

def sum_tuple(t):
    return sum(sum(inner) for inner in t if isinstance(inner, (list, tuple)))

tpl = ((1, 2), (3, 4), (5,))
print("Sum:", sum_tuple(tpl))
