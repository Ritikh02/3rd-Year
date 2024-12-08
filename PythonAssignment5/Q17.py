# 17. Using the sets {'red', 'green', 'blue'}, and {'cyan', 'green', 'blue', 'magenta', 'red'},
# display the results of:
set1 = {'red', 'green', 'blue'}
set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

# a) Comparing the sets using each of the comparison operators.
print(set1 == set2)
print(set1 != set2)
print(set1 < set2)
print(set1 <= set2)
print(set1 > set2)
print(set1 >= set2)

# b) Combining the sets using each of the mathematical set operators.
print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
print(set1 - set2)  # Difference (set1 - set2)
print(set2 - set1)  # Difference (set2 - set1)
print(set1 ^ set2)  # Symmetric difference