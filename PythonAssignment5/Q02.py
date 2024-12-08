# Q2. Write a program to enter names and percentage of marks in a dictionary and display the information on the screen.

student_dict = {}

while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name.lower() == "done":
        break
    percentage = float(input(f"Enter percentage of marks for {name}: "))
    student_dict[name] = percentage

print("Student Information:")
for name, percentage in student_dict.items():
    print(f"{name}: {percentage}%")
