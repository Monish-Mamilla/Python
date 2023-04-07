"""
Author: Monish Mamilla
Program Name: GCF
Date: 2/21/23
Version 1.0
"""
def gcf(num1, num2):
  factor = 1
  for x in range(1, num1 + 1):
    if num1 % x == 0 and num2 % x == 0:
      factor = x
  print("The greatest common factor of", num1, "and", num2, "is", factor)
# gets printed if the user enters 2 positive integers
number1 = int(input("Enter a positive integer: "))
number2 = int(input("Enter a positive integer: "))
# user will enter 2 positive integers
if number1 > 0 and number2 > 0:
  gcf(number1, number2)
else:
  print("Invalid input.")
# gets printed if the user doesn't enter a positive integer
