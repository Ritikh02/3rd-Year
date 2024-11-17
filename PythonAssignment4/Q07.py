# Write a function that takes a list of numbers as input from the user and produces the corresponding
# cumulative list where each element in the list at index i is the sum of elements at index j ≤ i.

lst = list(map(int, input("Enter list elements: ").split()))
cumulative = [sum(lst[:i+1]) for i in range(len(lst))]
print("Cumulative list:", cumulative)
