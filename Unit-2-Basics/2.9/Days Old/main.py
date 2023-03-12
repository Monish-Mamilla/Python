"""
Author: Monish Mamilla
Program Name: Days Old
Date: 11/14/22
"""
import datetime
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))
today = datetime.datetime.now()
curr = datetime.date(today.year, today.month, today.day)
birthday = datetime.date(year, month, day)
daysOld = (curr - birthday)
print(daysOld)
