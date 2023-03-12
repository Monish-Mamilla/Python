"""""
Author: Monish Mamilla
Program Name: Unit 2 Test
Date: 1 Nov 2022
Version 1.0
"""
import random
num1 = int(input("Enter a first number [1,100]: "))
num2 = int(input("Enter a second number [1,100]: "))
num3 = int(input("Enter a third number [1,100]: "))
#Enter three numbers
name1 = str(input("Enter your first name: "))
name2 = str(input("Enter your last name: "))
name3 = str(input("Name: "))
#Enter your first name, then last name, and finally full name.
start = 25
stop = 75
statement = random.randint(start,stop)
print("Random Number [{},{}]: {}".format(start,stop,statement))
#A random number between 25 and 75 will be printed
start = 10
stop = 50
step = 3
range = random.randrange(start,stop,step)
print ("Random Multiple of {} between [{},{}]: {}".format(step, start, stop, range))
#A random multiple of 3 between 10 and 50 will be printed
start = 100
stop = 1000
start = 1
stop = 100
var1 = random.randrange(start, stop)
var2 = random.randrange(start, stop)
var3 = var1 % var2
var4 = int(var1/var2)
print("{} / {} = {} R {}".format(var1, var2, var3, var4))
#Divide the first variable by the second variable and have the quotient/remainder show.
average = (num1 + num2 + num3)/3
average = round (average, 2)
print ("Average of {},{},and {}: {}".format(num1, num2, num3, average))
#The average of the 3 numbers inputted at the start will be printed.
