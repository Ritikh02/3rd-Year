# Question 16: Write a function to implement a basic calculator that can add, subtract, multiply, and divide two numbers based on user input.

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
print(calculator(num1, num2, operation))
