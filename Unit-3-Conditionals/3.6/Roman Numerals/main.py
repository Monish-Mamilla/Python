"""
Author: Monish Mamilla
Program Name: Roman Numerals
Date: 12/21/22
"""
num = int(input("Enter a number between [1,1000]: "))
if 1 <= num <= 1000:
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
# after the user enters a number between 1 and 1000, the digit entered for each place value determines the roman numeral
    if(hundreds==1):
        print('C', end='')
# the end function is used to print the roman numerals for each digit at once
    elif(hundreds==2):
        print('CC', end='')
    elif(hundreds==3):
        print('CCC', end='')
    elif(hundreds==4):
        print('CD', end='')
    elif (hundreds==5):
        print('D', end='')
    elif (hundreds==6):
        print('DC', end='')
    elif (hundreds==7):
        print('DCC', end='')
    elif (hundreds==8):
        print('DCCC', end='')
    elif (hundreds==9):
        print('CM', end='')
    else:
        print('M', end='')
# if the user didn't enter a digit for the hundreds place or entered 1000, then M will be printed
    if(tens==1):
        print('X', end='')
# if the user did not enter 1 for the digit in the tens place then a number in the elif or else chain will be printed
    elif(tens==2):
        print('XX', end='')
    elif(tens==3):
        print('XXX', end='')
    elif(tens==4):
        print('XL', end='')
    elif (tens==5):
        print('L', end='')
    elif (tens==6):
        print('LX', end='')
    elif (tens==7):
        print('LXX', end='')
    elif (tens==8):
        print('LXXX', end='')
    else:
        print('XC', end='')
    if(ones==1):
        print('I', end='')
    elif(ones==2):
        print('II', end='')
    elif(ones==3):
        print('III', end='')
    elif(ones==4):
        print('IV', end='')
    elif (ones==5):
        print('V', end='')
    elif (ones==6):
        print('VI', end='')
    elif (ones==7):
        print('VII', end='')
    elif (ones==8):
        print('VIII', end='')
    else:
        print('IX', end='')
else:
    print("Invalid number entered.")
# if the user did not enter a number between 1 and 1000, then the statement on line 72 will be printed
