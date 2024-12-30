import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll
# entering the amount of players and how many players are alowed to play the game
while True:
    players = input("Enter the number of players ( 2 - 4 ): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players. ")
    else:
        print("Invalid, try again.")

max_score = 100
player_scores = [0 for _ in range(players)]

# scoring system for the players
while max(player_scores) < max_score:

  for player_index in range(players):
    current_score = 0

while True:
  should_roll = input("Would you like to roll (y)? ")
  if should_roll.lower() != "y":
      break
  value = roll()
  if value == 1:
      print("You rolled a 1 turn over!")
  else:
      current_score += value
      print("You rolled a:", value)
  print("Your score is:", current_score)