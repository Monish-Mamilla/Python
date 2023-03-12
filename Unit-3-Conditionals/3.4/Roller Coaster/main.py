"""
Author: Monish Mamilla
Program Name: 3.4 Day 4 Do Now
Version: 1.0
Date: 12/6/22
"""
# looking to see if a user can ride the roller coaster
age = int(input("Enter your age: "))
if age > 12:
    oldEnough = True
    height = int(input("Enter your height (in inches): "))
    if height >= 48:
        tallEnough = True
    else:
        tallEnough = False
else:
    oldEnough = False

if oldEnough and tallEnough:
    print("Congrats! You can ride the roller coaster!")
else:
    print("Sorry, you are not able to ride the roller coaster :(")
    if not oldEnough:
        print("Come back when you're older!")
    else:
        print("Hopefully your growth spurt comes soon!")
