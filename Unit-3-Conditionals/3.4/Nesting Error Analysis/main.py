"""
Author: Monish Mamilla
Program Name: Nesting Error Analysis
Version: 1.0
Date: 12/5/22
"""
num = int(input("Enter a Number: "))
if num < 100:
num = input("Enter a number: ")
    if num > 10:
    num = input("Enter a number: ")
        if num % 7 != 0
        num = input("Enter a number: ")
            if num == "50":
            print("Winner!")
            else:
            print("Aw so close, you failed in the final round! :(")
        else:
        print("You failed round 3! :(")
    else:
    print("You failed round 2! :(")
else:
print("You failed round 1! :(")
