"""
Author: Monish Mamilla
Program Name: Prime Factorization
Date: 1/24/23
Version 1.0
"""
num = int(input("Enter a positive integer greater than or equal to 2: "))
# user will enter a number >= to 2
if num >= 2:
  factor = 2
  primeFacts = "{} = ".format(num)
  while factor < num:
    if num % factor == 0:
      primeFacts += "{}*".format(factor)
      num = num // factor
    else:
      factor += 1
  primeFacts += str(num)
  print(primeFacts)
else:
  print("Invalid input. Please enter a positive integer greater than or equal to 2.")
# if the user doesn't enter a number >= to 2, then the statement on line 21 will be printed
