# 16. Given the sets {10, 20, 30} and {5, 10, 15, 20}, use the mathematical set operators to produce the following sets:

set1 = {10, 20, 30}
set2 = {5, 10, 15, 20}

# a) {30}
result_a = set1 - set2
print(result_a)

# b) {5, 15, 30}
result_b = (set1 ^ set2)
print(result_b)

# c) {5, 10, 15, 20, 30}
result_c = set1 | set2
print(result_c)

# d) {10, 20}
result_d = set1 & set2
print(result_d)