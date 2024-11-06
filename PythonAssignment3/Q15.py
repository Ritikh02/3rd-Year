# Question 15: Create a function that returns the nth number in the Fibonacci sequence.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

user_n = int(input("Enter the position in Fibonacci sequence: "))
print(fibonacci(user_n))
