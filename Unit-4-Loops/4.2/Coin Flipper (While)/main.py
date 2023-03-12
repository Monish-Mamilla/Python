"""
Author: Monish Mamilla
Program Name: Coin Flipper
Version 2.0
Date: 1/17/23
"""
import random
numFlips = int(input("Enter the number of times to flip the coin: "))
# user will enter the number of times that they want the coin to be flipped
numHeads = 0
counter = 0
# numHeads and counter will be set to 0 at the start
while counter < numFlips:
    flip = random.randint(1, 2)
# the number generated, 1 or 2, determines whether the coin will land on heads of tails
    if flip == 1:
        numHeads += 1
    counter += 1
numTails = numFlips - numHeads
print("Number of heads flipped: ", numHeads)
print("Number of tails flipped: ", numTails)
# based on whether 1 or 2 was randomly generated, line 20 or line 21 will be printed
