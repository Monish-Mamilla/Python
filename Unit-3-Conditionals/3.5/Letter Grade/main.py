"""
Author: Monish Mamilla
Program Name: Letter Grade
Version 1.0
Date: 12/12/22
"""
numGrade = int(input("Enter your numerical grade: "))
if 0 <= numGrade <= 100:
# in order for either an if or elif statement to be printed, the user has to input a number between 0 and 100.
    if numGrade >= 90:
        print("Grade: A")
# if the user doesn't input a number between 90 and 100, then either the elif or else condition will be printed
    elif numGrade >= 80:
        print("Grade: B")
    elif numGrade >= 70:
        print("Grade: C")
    elif numGrade >= 65:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid Message, try again.")
# if the user doesn't input a number between 0 and 100, then the print statement on line 22 will be printed.
