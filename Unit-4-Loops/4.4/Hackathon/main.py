"""
Author: Monish Mamilla
Program Name: Random Lambda
Date: 3/6/23
Version 1.0
"""
import random
# Define the randomLambda function
randomLambda = lambda min, max: random.randint(min, max)
# Prompt the user for min and max values
min = int(input("Enter the min value: "))
max = int(input("Enter the max value: "))
# Call the randomLambda function and store the result in num
num = randomLambda(min, max)
# Print the value of num
print(num)
