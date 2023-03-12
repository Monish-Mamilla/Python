"""
Author: Monish Mamilla
Program Name: Pick A Card, Any Card Project
Date 1/6/23
Version 1.0
"""
import random
# Generate a random number between 1-52
random_number = random.randint(1, 52)
if random_number >= 1 and random_number <= 13:
# If the random number generated is 1, 11, 12, or 13, then one of the rank's will be printee
  suit = "Clubs"
  if random_number == 1:
    rank = "Ace"
  elif random_number == 11:
    rank = "Jack"
  elif random_number == 12:
    rank = "Queen"
  elif random_number == 13:
    rank = "King"
  else:
    rank = random_number
elif random_number >= 14 and random_number <= 26:
  suit = "Diamonds"
  if random_number == 14:
    rank = "Ace"
  elif random_number == 24:
    rank = "Jack"
  elif random_number == 25:
    rank = "Queen"
  elif random_number == 26:
    rank = "King"
  else:
    rank = random_number - 13
elif random_number >= 27 and random_number <= 39:
  suit = "Spades"
  if random_number == 27:
    rank = "Ace"
  elif random_number == 37:
    rank = "Jack"
  elif random_number == 38:
    rank = "Queen"
  elif random_number == 39:
    rank = "King"
  else:
    rank = random_number - 26
else:
  suit = "Hearts"
  if random_number == 40:
    rank = "Ace"
  elif random_number == 50:
    rank = "Jack"
  elif random_number == 51:
    rank = "Queen"
  elif random_number == 52:
    rank = "King"
  else:
    rank = random_number - 39
# The cards gets printed
print("Your card is the " + str(rank) + " of " + str(suit))
