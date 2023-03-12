"""
Author: Monish Mamilla
Program Name: Average (While)
Version 2.0
DateL 1/13/23
"""
size = int(input("Enter the size of the dataset: "))
# user will enter the dataset size
sum = 0
counter = 0
while counter < size:
    val = float(input("Enter the value: "))
# user will enter values for the average
    sum += val
    counter += 1
avg = sum / size
print("The average is:", avg)
# the average will be printed through line 15
