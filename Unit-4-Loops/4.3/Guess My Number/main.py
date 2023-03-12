"""
Author: Monish Mamilla
Program Name: Guess My Number
Date: 1/23/23
Version 1.0
"""
import random
replay = 1
while replay == 1:
  answer = random.randint(1, 100)
  numTries = 10
  guess = 0
  while guess != answer and numTries > 0:
    guess = int(input("Guess a number between 1 and 100: "))
# user will guess the number that the program has randomly generated
    if 1 <= guess <= 100:
      numTries -= 1
    if guess > answer:
      print("Too high!")
# if the program's number is lower than the user's number, then line 17 will be printed
    elif guess < answer:
      print("Too low!")
# if the program's number is higher than the user's number, then line 20 will be printed
    else:
      print("Correct!")
# line 23 will be printed, if the user's number and the program's number matches
  if numTries == 0:
    print("You lose! The answer was", answer)
  replay = int(input("Please enter if you would like to replay, \n1 - Yes\n2 - No"))

