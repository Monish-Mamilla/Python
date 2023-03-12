"""
Author: Monish Mamilla
Program Name: Letter Grade 2.0
Date: 11/16/22
"""
numGrade = int(input("Enter your numerical grade from 0 to 100: "))
ones = numGrade % 10
if numGrade >= 0 and numGrade<= 100:
    if numGrade == 100:
        print("A+")
# if the user enter 100 as their grade then the print statement above will be printed.
    if numGrade >= 90 and numGrade < 100:
        print('A', end='')
        if ones >= 0 and ones <= 2:
            print("-")
        elif ones >= 7 and ones <= 9:
            print("+")
# if the user enter a number between 90&100, then the ones digit will determine whether its the same or if it needs +/-
    elif numGrade >= 80 and numGrade < 90:
        print('B', end='')
        if ones >= 0 and ones <= 2:
            print("-")
        elif ones >= 7 and ones <= 9:
            print("+")
    elif numGrade >= 70 and numGrade < 80:
        print('C', end='')
        if ones >= 0 and ones <= 2:
            print("-")
        elif ones >= 7 and ones <= 9:
            print("+")
        elif numGrade >= 65 and numGrade < 70:
            print('D', end='')
# if the user didn't enter a number between 65 and 100, then their grade is an F or they wrote an invalid message.
        else:
            print('F', end='')
else:
    print("Invalid input message.")
