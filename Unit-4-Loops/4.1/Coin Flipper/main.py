"""
Author: Monish Mamilla
Program Name: Coin Flipper
Date: 1/10/23
Version 1.0
"""
import random
numFlips = int(input("Enter the number of times to flip the coin: "))
# user will enter the number of times that they want to flip a coin
numHeads = 0
for x in range (numFlips):
    flip = random.randint(1,2)
# random number generator will generate either 1 or 2
    if flip == 1:
        numHeads = numHeads + 1
numTails = numFlips - numHeads
# numTails will be numFlips subtracted by numHeads, which is a randomly generated value
print("Number Of Heads:",numHeads)
print("Number Of Tails:",numTails)
