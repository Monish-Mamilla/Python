"""
Author: Monish Mamilla
Program Name: Max and Min
Date: 2/21/23
Version 1.0
"""
def max(num1, num2):
  if num1 > num2:
    print("{} is the Max".format(num1))
# if num1 is greater than num2, then it is the max
  else:
    print("{} is the Max".format(num2))
# if num2 is greater than num1, then it is the max
def min(num1, num2):
  if num1 < num2:
    print("{} is the Min".format(num1))
  else:
    print("{} is the Min".format(num2))
# ask user to input two number
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
# check if equal, otherwise go to functions to print numbers
if num1 == num2:
  print("The numbers are equal.")
else:
  max(num1, num2)
  min(num1, num2)

