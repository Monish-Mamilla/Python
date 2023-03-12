"""
Author: Monish Mamilla
Program Name: Guess Your Number
Date: 2/1/23
Version 2.0
"""
replay = 1
while replay == 1:
  numTries = 0
  min = 1
  max = 100
  while numTries < 10:
    guess = (max + min) // 2
    response = input("Is " + str(guess) + ": 1. Too High 2. Too Low 3. Correct ")
    numTries += 1
    if response == "1":
      max = guess - 1
    elif response == "2":
      min = guess + 1
    else:
      print("Victory!")
# when the user gets the answer correctly, then line 21 will be printed
      break
  if numTries == 10:
    print("You cheated!")
  else:
    print("Thanks for playing.")
  replay = int(input("Play again? (1 for yes, 2 for no): "))
# the program will ask the user whether they want to continue or not
