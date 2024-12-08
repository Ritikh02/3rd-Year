# Modify a script to play 1,000,000 games of craps. Use two dictionaries, wins and losses, to track
# the number of games won and lost for each roll number. Update these dictionaries as the simulation progresses.

import random
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)
wins = {}
losses = {}

total_games = 1_000_000
for _ in range(total_games):
    roll_count = 0
    point = None

    while True:
        roll_count += 1
        roll = roll_dice()

        if roll_count == 1:
            if roll in (7, 11):
                wins[roll_count] = wins.get(roll_count, 0) + 1
                break
            elif roll in (2, 3, 12):
                losses[roll_count] = losses.get(roll_count, 0) + 1
                break
            else:
                point = roll
        else:
            if roll == point:
                wins[roll_count] = wins.get(roll_count, 0) + 1
                break
            elif roll == 7:
                losses[roll_count] = losses.get(roll_count, 0) + 1
                break

total_wins = sum(wins.values())
total_losses = sum(losses.values())

print(f"Percentage of wins: {total_wins / total_games * 100:.1f}%")
print(f"Percentage of losses: {total_losses / total_games * 100:.1f}%")

print("\nPercentage of wins/losses based on total number of rolls:")
print("Rolls | % Resolved on this roll | Cumulative % of games resolved")
print("---------------------------------------------------------------")

cumulative_games_resolved = 0

for roll in range(1, max(max(wins.keys(), default=0), max(losses.keys(), default=0)) + 1):
    resolved_on_roll = wins.get(roll, 0) + losses.get(roll, 0)
    percentage_resolved = (resolved_on_roll / total_games) * 100
    cumulative_games_resolved += resolved_on_roll
    cumulative_percentage = (cumulative_games_resolved / total_games) * 100

    print(f"{roll:<5} | {percentage_resolved:>20.2f}% | {cumulative_percentage:>30.2f}%")
