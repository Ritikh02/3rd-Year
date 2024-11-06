# Question 19: Create a function to find the greatest common divisor (GCD) of two numbers using a while loop.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(gcd(num1, num2))
