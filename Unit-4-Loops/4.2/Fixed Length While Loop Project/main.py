"""
Author: Monish Mamilla
Program Name: Fixed Length While Loop Project
Date: 1/19/23
Version 1.0
"""
import random
num_rolls = int(input("Enter the number of dice rolls: "))
# user will enter the number of times that they want to roll the dice
doubles_count = 0
x = 1
while x <= num_rolls:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
# the program will randomly choose a number from 1 to 6 to state as the number rolled for each dice
    if roll1 == roll2:
        print(f"{x}. {roll1} {roll2} DOUBLES")
# if the random number chosen for each dice by the program is the same, then DOUBLES will be printed next to it
        doubles_count += 1
    else:
        print(f"{x}. {roll1} {roll2}")
    x += 1
doubles_percent = (doubles_count / num_rolls) * 100
print(f"Number of doubles: {doubles_count} ({doubles_percent}%)")
# the percentage in line 23 and the double count will be printed

