"""
Author: Monish Mamilla
Program Name: Extra Loop Practice
Date: 2/14/23
Version 1.0
"""
pin = "1467"
# Set the PIN number
tries = 3
# Initialize the number of tries to 3
while tries > 0:
    guess = input("Enter your PIN number: ")
    if guess == pin:
        print("Success! You have entered the correct PIN.")
        break
# Exit the loop if the PIN is correct
    tries -= 1
# Decrement the number of tries remaining
    if tries > 0:
        print(f"Wrong PIN. You have {tries} attempt(s) left.")
    else:
        print("Sorry, you have run out of attempts. Access denied.")







