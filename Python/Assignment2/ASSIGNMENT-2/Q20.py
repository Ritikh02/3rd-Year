# Write a python program that reads an integer and displays all its smallest factors in increasing order.


num = int(input("Enter an integer: "))
factors = []

for i in range(2, num + 1):
    while num % i == 0:
        factors.append(i)
        num //= i

print(f"The smallest factors are: {', '.join(map(str, factors))}")
