"""
Author: Monish Mamilla
Program Name: Coin Streak
Date: 2/2/23
Version 1.0
"""
import random
replay = 1
longestStreak = 0
while replay == 1:
  streak = 0
  previous = 0
  flipNum = 1
  flip = 0
  while previous == flip:
    previous = flip
    flip = random.randint(1, 2)
    if flip == 1:
      print("Heads")
    else:
      print("Tails")
    if flipNum == 1:
      previous = flip
      flipNum += 1
    if flip == previous:
      streak += 1
      print("Current streak:", streak)
      if streak > longestStreak:
        longestStreak = streak
  replay = int(input("Play again? (1 for yes, 2 for no): "))
print("Longest streak:", longestStreak)
