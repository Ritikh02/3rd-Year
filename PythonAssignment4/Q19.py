# 19. Write a Python function to demonstrate the difference between shallow and deep copy of lists. 
# For example: 
# Original List: [['Shallow', 2, 3], [4, 5, 6]]
# Shallow Copy: [['Shallow', 2, 3], [4, 5, 6]]
# Deep Copy: [[1, 2, 3], ['Deep', 5, 6]]

import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0][0] = 'Shallow'
deep[1][0] = 'Deep'

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
