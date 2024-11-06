# Write a program such that Python will ask you if it is raining or not. If your answer is ”yes”, Python
#will say ”Carry an umbrella”. If you say ”no”, Python will say ”No need to carry an umbrella”. If
#you type anything else, Python will say ”Bye”.

answer = input("Is it raining? (yes/no): ")

if answer.lower() == "yes":
    print("Carry an umbrella")
elif answer.lower() == "no":
    print("No need to carry an umbrella")
else:
    print("Bye")

