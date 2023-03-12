"""
Author: Monish Mamilla
Program Name: Factors of a Number
Date: 1/12/23
Version 1.0
"""
num = int(input("Enter a non-negative integer: "))
# user will enter a non-negative integer
if num >= 0:
    factors = "      "
    for x in range(1, num):
        value = num // x
# value will determine all the values that are divisible by num
        if value:
            allvalues = factors + str(value)
#allvalues will contain all the integers that are factors to "num"
            print(allvalues)
