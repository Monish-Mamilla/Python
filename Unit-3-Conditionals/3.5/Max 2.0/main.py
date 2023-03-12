"""
Author: Monish Mamilla
Program Name: Max
Version 2.0
Date: 12/9/22
"""
num1 = int(input("Enter a number: "))
num2= int(input("Enter another number: "))
if num1 > num2:
    print("Num1 is larger.")
# if the user's first number is greater than their second number, then the print statement above will be printed
elif num2 > num1:
    print("Num2 is larger.")
# if the user's second number is greater than their first number, then the print statement in line 13 will be printed
else:
    print("Both numbers are equal!")
# if either condition above is not met, then the print statement for the else condition will be printed
