import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll
while True:
    players = input("Enter the number of players ( 1 - 4 ): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 1 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 100
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
  pass

