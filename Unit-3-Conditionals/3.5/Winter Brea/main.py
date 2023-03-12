"""
Author: Monish Mamilla
Program Name: Winter Break
12/9/22
Version 1.0
"""
day = input("Enter which day of the week Christmas/New Years is on: ")
if day == "Sunday":
    print("The break is 9 days and they are 12/24, 12/25, 12/26, 12/27, 12/28, 12/29, 12/30, 12/31, and 1/1.")
# if the user enters "Sunday" then the statement above will be printed
# if the statement above is not met, then the elif condition will be printed based on which day of the week they entered
elif day == "Monday":
    print("The break is 10 days and they are 12/23, 12/24, 12/25, 12/26, 12/27, 12/28, 12/29, 12/30, 12/31, and 1/1.")
elif day == "Tuesday":
    print("The break is 11 days and they are 12/22, 12/23, 12/24, 12/25, 12/26, 12/27, 12/28, 12/29, 12/30, 12/31, and 1/1.")
elif day == "Wednesday":
    print("The break is 9 days and they are 12/24, 12/25, 12/26, 12/27, 12/28, 12/29, 12/30, 12/31, and 1/1.")
elif day == "Thursday":
    print("The break is 9 days and they are 12/24, 12/25, 12/26, 12/27, 12/28, 12/29, 12/30, 12/31, and 1/1.")
elif day == "Friday":
    print("The break is 11 days and they are 12/24, 12/25, 12/26, 12/27, 12/28, 12/29, 12/30, 12/31, 1/1, 1/2, and 1/3.")
elif day == "Saturday":
    print("The break is 11 days and they are 12/24, 12/25, 12/26, 12/27, 12/28, 12/29, 12/30, 12/31, 1/1, 1/2, and 1/3.")
# if the user did not meet the if or elif statements, then the print statement below will be printed.
else:
    print("Invalid Message.")

