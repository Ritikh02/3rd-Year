#Write a Python program to calculate a student’s letter grade based on their numeric score using the following scale: A (90–100), B (80–89), C (70–79), D (60–69), and F (below 60). Additionally, provide
#a comment for each grade: ”Excellent” for A, ”Good” for B, ”Average” for C, ”Needs Improvement”
#for D, and ”Failing” for F.

score = int(input("Enter the student's numeric score: "))

if 90 <= score <= 100:
    grade = "A"
    comment = "Excellent"
elif 80 <= score <= 89:
    grade = "B"
    comment = "Good"
elif 70 <= score <= 79:
    grade = "C"
    comment = "Average"
elif 60 <= score <= 69:
    grade = "D"
    comment = "Needs Improvement"
else:
    grade = "F"
    comment = "Failing"

print(f"Grade: {grade}, Comment: {comment}")
