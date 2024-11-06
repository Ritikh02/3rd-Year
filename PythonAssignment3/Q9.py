# Question 9: Write two functions, one of which converts a binary number to decimal and the other one does the reverse.

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

user_binary = input("Enter a binary number: ")
print(binary_to_decimal(user_binary))

user_decimal = int(input("Enter a decimal number: "))
print(decimal_to_binary(user_decimal))
