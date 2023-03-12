"""
Author: Monish Mamilla
Program Name: 3.1-3.5 Project
Version 1.0
Date: 12/15/22
"""
import math
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
# user will input a value for variables a,b, and c
d = (b**2) -(4*a*c)
e = "="
print ("{}x^2 + {}x + {} {} 0".format(a, b, c,e))
if d < 0:
    print("There are 2 imaginary solutions.")
# if d(discriminant) is less than 0, then the print statement above will be printed
elif d > 0:
    print("There are 2 real solutions.")
    print("x = {} and x = {}".format((-b-math.sqrt(d))/(2*a),(-b+math.sqrt(d))/(2*a)))
# if d(discriminant) is greater than 0, then the print statement on line 19 will be printed
else:
    print("There is 1 real solution.")
    print("x = {}".format((-b-math.sqrt(d))/(2*a)))
# if d(discriminant) is neither less than 0 or greater than 0, then the print statement on line 23 will be printed
