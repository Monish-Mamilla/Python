"""
Author: Monish Mamilla
Program Name: 12/13/22
Version 1.0
Date: 12/13/22
"""
import math
print("1. Distance Formula")
print("2. Heron's Formula")
print("3. Temperature Conversion")
print("4. Pythagorean Theorem")
# the user will choose between one of these 6 choices
choice = input("Choose one of these 4 (Type word for word): ")
if choice == "Distance Formula":
    x1 = int(input("Type in x1: "))
    y1 = int(input("Type in y1: "))
    x2 = int(input("Type in x2: "))
    y2 = int(input("Type in y2: "))
    distance = math.sqrt((x2-x1)) ** 2 + (y2-y1) ** 2
    print("coordinates: " + str(x1) + "," + str(x2) +"," + str(y1) + "," +str(y2))
    print("Distance: " + str(distance))
# if the user doesn't choose "Distance Formula" then one of the elif conditions will be printed
elif choice == "Heron's Formula":
    herA = int(input("Enter a side length of the triangle: "))
    herB = int(input("Enter a side length of the triangle: "))
    herC =int(input("Enter a side length of the triangle: "))
    semiP = (herA+herB+herC)/2
    area = semiP * (semiP -herA) * (semiP - herB) * (semiP-herC)
    print("Area: " + str(area))
elif choice == "Temperature Conversion":
    state1 = "C -> F"
    state2 = "F -> C"
    choice1 = input("Choose one of these 2 for Temperature Conversion (Type word for word): ")
    if choice1 == "Convert C - > F":
        tempC = int(input("Enter the input in Celsius: "))
        tempF = tempC * 1.8 + 32
        print("Celsius: {}  Fahrenheit: {}".format(tempC,tempF))
    else:
        tempF = input("Enter the input in Fahrenheit: ")
        tempC = tempF * 32 * 0.665
            print("Fahrenheit {}  Celcius: {}".format(tempF,tempC))
elif choice == "Pythagorean Theorem":
    c1 = "Pythagorean Theorem - Leg"
    c2 = "Pythagorean Theorem - Hypotenuse"
elif choice == "Pythagorean Theorem - Leg":
    pyA = int(input("Enter 1st known leg length: "))
    pyC = int(input("Enter 2nd known leg length: "))
    pyB = math.sqrt((pyA ** 2 - pyC ** 2))
    print (pyB)
elif choice == "Pythagorean Theorem - Hypotenuse":
    pya = int(input("Enter 1st known leg length: "))
    pyb = int(input("Enter 2nd known leg length: "))
    pyc = math.sqrt((pya ** 2 - pyB ** 2))
    print (pyC)
