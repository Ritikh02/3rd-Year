# Question 2: Find the numbers between 100 and 500, which are divisible by 3 and multiples of 5 using function in Python.

def find_numbers():
    result = [num for num in range(100, 501) if num % 3 == 0 and num % 5 == 0]
    return result

print(find_numbers())
