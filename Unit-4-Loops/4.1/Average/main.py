"""
Author: Monish Mamilla
Program Name: Average
Date: 1/11/23
Version 1.0
"""
size = int(input("Enter the size of the dataset in order to find the average: "))
# this will give the number of values needed to calculate the average
sum = 0
for x in range(size):
    val = int(input("Enter the value: "))
    sum = sum + val
avg = sum / size
# avg will be calculated through sum and size from user values
print (avg)
