"""
Author: Monish Mamilla
Program Name: Task #2 - Fixed Length While Loop
Date: 1/26/23
Version 1.0
"""
num_periods = int(input("How many class periods do you have in your schedule? "))
# Create an empty list to store the class names
schedule = []
while schedule < num_periods + 1:
    num_periods = num_periods + 1
# Ask the user for the class name for each period
class_name = input(f"Enter class for Period {num_periods}: ")
# Append the class name to the schedule list
schedule.append(class_name)
# Print out the entire schedule
print(f"Period {num_periods}: {class_name}")
