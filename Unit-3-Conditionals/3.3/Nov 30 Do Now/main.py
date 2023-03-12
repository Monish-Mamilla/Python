"""
Author: Monish Mamilla
Program Name: 11/30/22
Date: 11/30/22
Version 1.0
"""
number = int(input("Enter a Number: "))
if number > 5 and number < 19 and number % 3 == 0:
    print("{} is in [6, 18] and divisible by 3!".format(number))
multiple3 = number > 5 and number < 19 and number % 3 == 0
if multiple3 == True:
    print("{} is in [6, 18] and divisible by 3!".format(number))
if multiple3:
    print("{} is in [6, 18] and divisible by 3!".format(number))
else:
    print("{} is not a multiple of 3 in [6, 18]!".format(number))
