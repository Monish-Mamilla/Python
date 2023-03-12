"""
Author: Monish Mamilla
Date: 11/18/22
Program Name: Which Number is Bigger?
Version 1.0
"""
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
same = num1 == num2
if same:
    print("The numbers are the same.")
#The statement above will be printed if the user inputs the same number for both.
if num1 > num2:
    print("Num1 is larger.")
#The statement above will be printed if num1 is greater than num2.
if num2 > num1:
    print("Num2 is larger.")
#The statement above will be printed if num2 is greater than num1.
