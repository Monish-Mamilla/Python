"""
Author: Monish Mamilla
Program Name: Leap Year
Version 1.0
Date: 12/6/22
"""
import datetime
print("Options: ")
print("1. Check the Current Year")
#If the user enters 1, 2022 will be checked to see if it is a leap year.
print("2. Input a year.")
#If the user enter 2, they can choose any year to be checked, in order to see if it is a leap year.
choice = int(input("Select an option from the list above: "))
if choice == 1:
    year = date.today().year
else:
    year = int(input("Enter the year that you want to check: "))
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if leap_year:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
