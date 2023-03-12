"""
Author: Monish Mamilla
Program Name: 12/6/22
Date: 12/6/22
"""
school_today = False
weekend = input("Is it the weekend (Saturday or Sunday): ")
if weekend == "No":
    holiday = input("Is it a holiday: ")
    if holiday == "No":
        sch_break = input("Is it a summer, winter, or spring break: ")
        if sch_break == "no":
            school_today = True
#If all the conditions above are "No", then there is school today.
        else:
            school_today = False
#If a condition above is "Yes," then there is no school today.
    else:
        school_today = False
else:
    school_today = False
if school_today:
    print("There is no school today!")
else:
    print("There is school today!")
