"""
Author: Monish Mamilla
Program Name: Test Score Prediction
Date: 28 Oct 2022
Version 1.0
"""

import random
hoursDistracted = int(input("Enter the number of hours you are distracted: "))
#Number of hours distracted
hoursStudy = int(input("Enter the number of hours you have studied for: "))
#Number of hours studied
hoursSlept = int(input("Enter the number of hours you sleep for: "))
#Number of hours slept
maximum = 100 - (5 * hoursDistracted)
minimum = 50 + (2 * hoursStudy) + (5 * hoursSlept)
prediction = random.randint(maximum,minimum)
print ("Your test score will probably be {}.".format(prediction))
