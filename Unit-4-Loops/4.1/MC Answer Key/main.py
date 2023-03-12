"""
Author: Monish Mamilla
Program Name: MC Answer Key
Date: 1/9/23
Version 1.0
"""
import random
numQuestions = int(input("Enter the number of questions on the test: "))
# user will enter the number on questions on their test
for x in range(numQuestions):
    randNum = random.randint(1,4)
# randNum will generate 1, 2, 3, 4 randomly, and based on the number A, B, C, D will printed
    value = x + 1
    value = str(value)+str(".")
    if randNum == 1:
        print(value+ "A")
    elif randNum == 2:
        print(value+ "B")
    elif randNum == 3:
        print(value+ "C")
# if none of the statements above are printed, then the statement below will be printed
    else:
        print(value+"D")
