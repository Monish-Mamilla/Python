"""
Author: Monish Mamilla
Program Name: LCM and GCF
Date: 3/2/23
Version 2.0
"""
def gcf(num1, num2):
    factor = 1
    for x in range(1, num1+1):
        if num1 % x == 0 and num2 % x == 0:
            factor = x
    return factor
def lcm(num1, num2):
    mult = num1 * num2
    fact = gcf(num1, num2)
    mult = mult / fact
    return mult
choice = input("Enter 'G' to find the GCF, or 'L' to find the LCM: ")
if choice == "G":
    num1 = int(input("Enter the first positive integer: "))
    num2 = int(input("Enter the second positive integer: "))
# user will enter 2 positive integers for GCF
    if num1 > 0 and num2 > 0:
        gcFact = gcf(num1, num2)
        print(f"The GCF of {num1} and {num2} is {gcFact}")
    else:
        print("Invalid input. Please enter positive integers only.")
elif choice == "L":
    num1 = int(input("Enter the first positive integer: "))
    num2 = int(input("Enter the second positive integer: "))
    if num1 > 0 and num2 > 0:
        lcMult = lcm(num1, num2)
        print(f"The LCM of {num1} and {num2} is {lcMult}")
    else:
        print("Invalid input. Please enter positive integers only.")
# if the user doesn't enter a positive integer, then line 35 will be printed
else:
    print("Invalid selection. Please enter 'G' or 'L' only.")
