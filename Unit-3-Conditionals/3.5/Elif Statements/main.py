"""
Author: Monish Mamilla
Program Name: Elif Statements
Version 1.0
Date: 12/9/22
"""
num = int(input("Enter a number: "))
if num == 5:
    print("You guessed my lucky number!")
# if the user prints 5, the statement above will be printed
elif num > 5:
    print("My lucky number isn't that big, try again.")
# if the user prints a number greater than 5, the statement in line 12 will be printed
else:
    print("Sorry wrong number, try again.")
# if the user doesn't meet the requirement of either of the two above statements, the statement in line 15 gets printed
