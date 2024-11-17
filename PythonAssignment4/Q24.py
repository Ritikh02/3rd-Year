# Question: Given a list of tuples, remove all the tuples with length K, where K is user-defined.

def remove_tuples_of_length(lst, K):
    return [tup for tup in lst if len(tup) != K]
tuples_list = [(1, 2), (3, 4, 5), (6, 7, 8, 9), (10, 11), (12,)]
K = int(input("Enter the length of tuples to remove: "))
result = remove_tuples_of_length(tuples_list, K)
print("List after removal:", result)
