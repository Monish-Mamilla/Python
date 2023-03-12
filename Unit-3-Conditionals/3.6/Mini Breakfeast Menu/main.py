"""
Author: Monish Mamilla
Program Name: Mini Breakfeast
Description: Practice printing multiple things on one line
Date: 12/20/22
Version: 1.0
"""
# give user a mini food menu
breakfast = int(input("For Breakfast:"
                  "\n1 - Bagel"
                  "\n2 - Cereal"
                  "\n3 - Fruit\n"))
if breakfast == 1:
    breakfastChoice = "Bagel"
elif breakfast == 2:
    breakfastChoice = "Cereal"
elif breakfast == 3:
    breakfastChoice = "Fruit"

if 1 <= breakfast <= 3:
    drink = int(input("Add a Drink:"
              "\n1 - Coffee"
              "\n2 - Water"
              "\n3 - Juice\n"))
    if drink == 1:
        breakfastChoice = breakfastChoice + " and Coffee"
    elif drink == 2:
        breakfastChoice = breakfastChoice + " and Water"
    elif drink == 3:
        breakfastChoice = breakfastChoice + " and Juice"

    if 1 <= drink <= 3:
        print("Your breakfast order is: " + breakfastChoice)
else:
    print("Invalid input")
