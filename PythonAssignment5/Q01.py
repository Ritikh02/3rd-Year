# Q1. Write a program to accept student name and marks from the user and create a dictionary. 
# Also, display student marks by taking student name as input.

student_dict = {}

while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name.lower() == "done":
        break
    marks = int(input(f"Enter marks for {name}: "))
    student_dict[name] = marks

search_name = input("Enter the name of the student whose marks you want to find: ")
if search_name in student_dict:
    print(f"{search_name}'s marks: {student_dict[search_name]}")
else:
    print(f"Student {search_name} not found in the record.")
