# Write a Python program that calculates the final cost of a hotel booking based on the room type, length of stay, season, and loyalty member status.


room_type = input("Enter room type (Standard, Deluxe, Suite): ")
length_of_stay = int(input("Enter length of stay in nights: "))
season = input("Enter season (Peak, Off, Regular): ")
loyalty_member = input("Are you a loyalty member? (yes/no): ")

room_prices = {"Standard": 100, "Deluxe": 150, "Suite": 250}
base_cost = room_prices[room_type] * length_of_stay

if length_of_stay > 7:
    base_cost *= 0.8
elif length_of_stay > 3:
    base_cost *= 0.9

if season == "Peak":
    base_cost *= 1.2
elif season == "Off":
    base_cost *= 0.85

if loyalty_member.lower() == "yes":
    base_cost *= 0.95

print(f"The final booking cost is: ${base_cost:.2f}")
