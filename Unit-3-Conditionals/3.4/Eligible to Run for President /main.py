"""
Author: Monish Mamilla
Program Name: Eligible To Run For President
Version 1.0
Date: 12/5/22
"""
eligible = True
age = int(input("Enter your age: "))
if age >= 35:
    citizen = input("Are you a natural born citizen: ")
    if citizen == "Yes":
        resident = input("Have you been a legal resident for the past 14 years: ")
        if resident == "Yes":
            terms = input("Enter the number of terms you have previously served as president: ")
            if terms < "2":
                eligible = True
            else:
                eligible = False
        else:
            eligible = False
    else:
        eligible = False
else:
    eligible = False
if eligible:
    print("You are eligible to run for president!")
#If all the conditions above are met, then you (user) are eligible to run for president.
else:
    print("You are not eligible to run for president.")
#If all the conditions above are not met, then you (user) are not eligible to run for president.
