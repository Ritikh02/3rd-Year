# 18. You are given two lists of integers: list1 and list2. Write a Python function analyze_sets(list1, list2)
# that performs the described tasks.

def analyze_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    symmetric_difference = set1 ^ set2
    modified_elements = []

    for elem in symmetric_difference:
        if elem % 2 == 0:
            modified_elements.append(elem * 2)
        else:
            modified_elements.append(elem + 5)

    return sorted(modified_elements)

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = analyze_sets(list1, list2)
print(result)