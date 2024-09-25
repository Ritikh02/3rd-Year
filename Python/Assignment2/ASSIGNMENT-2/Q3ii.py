# Write a program that reads the lengths of the three sides of a triangle from the user. Then display a
# message that states the triangles type

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side2 == side3 or side1 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"

print(f"The triangle is {triangle_type}.")
