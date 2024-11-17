# Question a)
# Mistake: The tuple has 3 elements, but only 2 variables are provided for unpacking.
# Output: ValueError: too many values to unpack (expected 2)
day, high_temperature = ('Monday', 87, 65)

# Question b)
# Mistake: The list only has indices 0-4, so index 10 does not exist.
# Output: IndexError: list index out of range
numbers = [1, 2, 3, 4, 5]
print(numbers[10])

# Question c)
# Mistake: Strings are immutable; we cannot modify their content directly.
# Output: TypeError: 'str' object does not support item assignment
name = 'amanda'
name[0] = 'A'

# Question d)
# Mistake: List indices must be integers, not floats.
# Output: TypeError: list indices must be integers or slices, not float
numbers = [1, 2, 3, 4, 5]
print(numbers[3.4])

# Question e)
# Mistake: Tuples are immutable; their elements cannot be changed.
# Output: TypeError: 'tuple' object does not support item assignment
student_tuple = ('Amanda', 'Blue', [98, 75, 87])
student_tuple[0] = 'Ariana'

# Question f)
# Mistake: Tuples and strings cannot be concatenated directly.
# Output: TypeError: can only concatenate tuple (not "str") to tuple
print(('Monday', 87, 65) + 'Tuesday')

# Question g)
# Mistake: Strings and tuples cannot be concatenated directly.
# Output: TypeError: can only concatenate str (not "tuple") to str
print('A' + ('B', 'C'))

# Question h)
# Mistake: 'x' is deleted, so trying to access it raises an error.
# Output: NameError: name 'x' is not defined
x = 7
del x
print(x)

# Question i)
# Mistake: '10' is not in the list, so it raises an error.
# Output: ValueError: 10 is not in list
numbers = [1, 2, 3, 4, 5]
print(numbers.index(10))

# Question j)
# Mistake: extend() expects an iterable (e.g., list or tuple), not separate arguments.
# Output: TypeError: extend() takes exactly one argument (3 given)
numbers = [1, 2, 3, 4, 5]
numbers.extend(6, 7, 8)

# Question k)
# Mistake: '10' is not in the list, so remove() raises an error.
# Output: ValueError: list.remove(x): x not in list
numbers = [1, 2, 3, 4, 5]
numbers.remove(10)

# Question l)
# Mistake: Cannot pop from an empty list.
# Output: IndexError: pop from empty list
values = []
values.pop()
