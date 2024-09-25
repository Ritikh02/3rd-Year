# Write a program that reads a position from the user and identifies the proper color of the respective box.

position = input("Enter a chess position (e.g., e4): ")

column = position[0]
row = int(position[1])

# Calculate the color of the box
if (ord(column) - ord('a') + row) % 2 == 0:
    color = "black"
else:
    color = "white"

print(f"The color of the box at {position} is {color}.")
