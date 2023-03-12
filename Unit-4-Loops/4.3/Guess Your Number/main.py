"""
Author: Monish Mamilla
Program Name: Guess Your Number
Date: 1/24/23
Version 1.0
"""
numTries = 0
min = 1
max = 100
while numTries < 10:
  guess = (max + min) // 2
  print(guess)
  response = input("Is the guess too high, too low, or correct? (Type high, low, or correct):")
# user will decide whether the program's number is high, low, or correct
  numTries += 1
  if response == "high":
    max = guess - 1
  elif response == "low":
    min = guess + 1
  elif response == "correct":
    print("Victory! I found the number in", numTries, "tries.")
# when the user gets the correct, answer line 21 will be printed
    break
  else:
    print("Invalid input. Please type high, low, or correct.")
# if the user doesn't enter one of three terms above, then line 25 will be printed
if numTries < 10:
  print("Thanks for playing!")
else:
  print("You lose! I couldn't find the number in", numTries, "tries.")
