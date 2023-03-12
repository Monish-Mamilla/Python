"""
Author: Monish Mamilla
Program Name: Triangle Inequality Theorem
Date: 11/29/22
Version 1.0
"""
side1 = float(input("Enter the side length:  "))
side2 = float(input("Enter the side length:  "))
side3 = float(input("Enter the side length:  "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#if all the conditions above are met, then the print statement below will be printed
    print("The segments can form a triangle.")
else:
    print("The segments cannot form a triangle.")
#if all the conditions on line 10 are not met, then the print statement above will be printed
