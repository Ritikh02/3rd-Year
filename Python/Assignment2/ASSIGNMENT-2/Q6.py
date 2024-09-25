# Write a program that takes an integer input from the user and prints whether it is prime or not


num = int(input("Enter an integer: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
else:
    print("The number is not prime")
