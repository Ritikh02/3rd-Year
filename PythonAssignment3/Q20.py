# Question 20: Write a function to print all prime numbers between 1 and 100.

def print_primes():
    primes = [num for num in range(2, 101) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return primes

print(print_primes())
