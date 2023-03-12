"""
Author: Monish Mamilla
Program Name: Factors of a Number (While)
Version 2.0
Date: 1/17/23
"""
num = int(input("Enter a non-negative integer: "))
# user is supposed to input a non-negative number
if num >= 0:
    factors = ""
    counter = 1
    while counter < num:
        if num % counter == 0:
            factors += str(counter) + ","
        counter += 1
    factors += str(num)
    print("Factors of " + str(num) + ": " + factors)
# line 17 will state all the factors from the number that the user inputted
else:
    print("Invalid entry. Please enter a non-negative integer.")
# if the user doesn't input a number >=0, then line 20 will be printed
