# Write a program to compute the sum of all prime numbers below a user input number


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = int(input("Enter a number: "))
prime_sum = sum(num for num in range(2, limit) if is_prime(num))

print(f"The sum of all prime numbers less than {limit} is {prime_sum}")
