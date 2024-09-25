# Write a program that functions as a simple calculator and continues until the user types "exit"


while True:
    user_input = input("Enter two numbers and an operator (+, -, *, /) or type 'exit' to quit: ").split()
    if user_input[0].lower() == "exit":
        break
    try:
        num1, num2 = float(user_input[0]), float(user_input[1])
        operator = user_input[2]
        match operator:
            case "+":
                print(num1 + num2)
            case "-":
                print(num1 - num2)
            case "*":
                print(num1 * num2)
            case "/":
                print(num1 / num2 if num2 != 0 else "Cannot divide by zero")
            case _:
                print("Invalid operator")
    except (ValueError, IndexError):
        print("Invalid input")
