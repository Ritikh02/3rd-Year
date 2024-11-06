# Question 29: Write a function to check if a given number is a perfect number. (A number is called a perfect number if it is equal to the sum of its real divisors, e.g., 6=1+2+3, 28=1+2+4+7+14).

def is_perfect_number(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

user_number = int(input("Enter a number: "))
print(is_perfect_number(user_number))
