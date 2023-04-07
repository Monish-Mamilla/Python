"""
Author: Monish Mamilla
Program Name: Room Painter Project
Date: 3/2/23
Version 1.0
"""
def getCost(length, width, height, numWindows, numDoors):
# the 5 parameters will be calculated with the formulas in lines 10 to 16
    wallArea = 2 * (length * height + width * height) - (12 * numWindows + 20 * numDoors)
    ceilingArea = width * length
    wallCost = 0.50 * wallArea
    ceilingCost = 0.25 * ceilingArea
    windowTrimCost = 2 * numWindows
    doorTrimCost = 3 * numDoors
    totalCost = wallCost + ceilingCost + windowTrimCost + doorTrimCost
    return totalCost
# Main body of the program
length = float(input("Enter the length of the room: "))
width = float(input("Enter the width of the room: "))
height = float(input("Enter the height of the room: "))
numWindows = int(input("Enter number of windows: "))
numDoors = int(input("Enter number of doors: "))
# user will have to enter the length, width, height, number of windows, and number of doors in their room
totalCost = getCost(length, width, height, numWindows, numDoors)
print("The total cost to paint the room is ${:.2f}".format(totalCost))
# total cost will be printed from the parameters that the user gave


