# Question 3: Write a Python function to add the squares of the even numbers between 1 and 50 (both included).

def sum_of_squares():
    result = sum(num ** 2 for num in range(1, 51) if num % 2 == 0)
    return result

print(sum_of_squares())
