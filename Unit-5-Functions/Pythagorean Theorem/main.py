"""
Author: Monish Mamilla
Program Name: Pythagorean Theorem
Date: 3/2/23
Version 2.0
"""
import math
def pyLeg(a, c):
    b = math.sqrt(c**2 - a**2)
# formula to find missing leg
    return b
def pyHyp(a, b):
    c = math.sqrt(a**2 + b**2)
# formula to find hypotenuse
    return c
choice = input("Enter leg or hypotenuse: ")
# user will enter either leg or hypotenuse to solve for
if choice == "leg":
    sideA = float(input("Enter the length of the known leg: "))
    sideC = float(input("Enter the length of the hypotenuse: "))
    sideB = pyLeg(sideA, sideC)
# missing side length will be calculated through the formula on line 9
    print(f"The length of the missing leg is {sideB:.2f}")
elif choice == "hypotenuse":
    sideA = float(input("Enter the length of one of the legs: "))
    sideB = float(input("Enter the length of the other leg: "))
    sideC = pyHyp(sideA, sideB)
# hypotenuse will be calculated through the formula on line 13
    print(f"The length of the hypotenuse is {sideC:.2f}")
else:
    print("Invalid choice. Please enter 'leg' or 'hypotenuse' only.")
