"""
Author: Monish Mamilla
Program Name: Max
Version 1.0
Date: 12/5/22
"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 == num2:
    print("The numbers are equal.")
#If the numbers inputted are equal, then the statement above will be printed.
else:
    if num1 > num2:
        print("Num1 is larger.")
#If the first number inputted is greater than the second number inputted, then the statement in line 14 will be printed.
    else:
        print("Num2 is larger.")
#If the if statement and first else statement is false, then the statement in line 17 will be printed.
