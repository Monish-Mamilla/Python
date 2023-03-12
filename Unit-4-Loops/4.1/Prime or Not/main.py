"""
Author: Monish Mamilla
Program Name: Prime or Not
Date: 1/11/22
Version 1.0
"""
num = int(input("Enter an integer greater than or equal to 2: "))
# user has to input an integer that is >= to 2
if num >= 2:
    prime = True
    for x in range(2,num):
        if num % x == 0:
            prime = False
            break
    if prime == True:
        print("Num is prime.")
    else:
        print("Num is composite.")
# if prime is not true, then the print statement on line 17 will be printed
else:
    print("Invalid entry message.")
# if the user didn't enter a number that was >= 2, then the print statement on line 19 will be printed
