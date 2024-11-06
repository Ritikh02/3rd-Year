# Question 25: Write a function to check if two numbers are coprime.

def are_coprime(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return gcd(a, b) == 1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(are_coprime(num1, num2))
