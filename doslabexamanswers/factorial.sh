# Question 1: Write a shell script that calculates the factorial of a given number n.
# The number n is passed as a command-line argument.

#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

n=$1
factorial=1

for (( i=1; i<=n; i++ )); do
    factorial=$((factorial * i))
done

echo "Factorial of $n is $factorial"

# Run using bash factorial.sh <number>
