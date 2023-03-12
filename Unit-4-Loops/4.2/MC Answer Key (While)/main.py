"""
Author: Monish Mamilla
Program Name: MC Answer Key (While)
Version 2.0
Date: 1/13/23
"""
import random
# import random will be used
numQuestions = int(input("Enter the number of questions on the test: "))
# user will enter the number of questions on their test
counter = 1
while counter <= numQuestions:
    randNum = random.randint(1, 4)
# a random number between 1 and 4 will determine which grade they get
    if randNum == 1:
        print("Question", counter, ": A")
    elif randNum == 2:
        print("Question", counter, ": B")
    elif randNum == 3:
        print("Question", counter, ": C")
    else:
        print("Question", counter, ": D")
    counter += 1
