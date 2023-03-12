"""
Author: Monish Mamilla
Program Name: Number Match
Date: 1/25/23
Version 1.0
"""
import random
num = int(input("Enter a number between 1 and 100: "))
# user will enter a number between 1 and 100
if 1 <= num <= 100:
  numTries = 0
  guess = 0
  while num != guess:
    guess = random.randint(1, 100)
# program will "guess" what the user's number is from 1 to 100
    numTries += 1
    print(f"Attempt {numTries}: {guess}")
  print(f"It took {numTries} attempts to match the number {num}.")
# the program will run random numbers until it matches with the user's number
else:
  print("Invalid input. Please enter a number between 1 and 100.")
# if the user doesn't enter a number between 1 and 100, then the message on line 21 will be printed
