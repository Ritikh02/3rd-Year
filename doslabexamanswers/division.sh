# Question 3: Shell script to calculate the division based on marks in 5 subjects.

#!/bin/bash

echo "Enter marks for 5 subjects:"
read -a marks

total=0
for mark in "${marks[@]}"; do
    total=$((total + mark))
done

percentage=$((total / 5))

if [ $percentage -ge 60 ]; then
    division="First Division"
elif [ $percentage -ge 50 ]; then
    division="Second Division"
elif [ $percentage -ge 40 ]; then
    division="Third Division"
else
    division="Fail"
fi

echo "Total: $total, Percentage: $percentage%, Division: $division"

#to run bash division.sh
