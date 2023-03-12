"""
Author: Monish Mamilla
Program name: Hackathon (Food Menu)
Description: Let the user choose their meal and use if statements to find the total costs
Date: 11/18/22
Version: 1.0
"""
print("Welcome to Monish's Restaurant!")
drink = int(input("Drink Options:\n1 - Soda ($2)\n2 - Juice ($1.75)\n"
                  "3 - Lemonade ($2.25)\n4 - Water/no drink (Free)\n"))
appetizer = int(input("Appetizer Options:\n1 - Wings ($7)\n2 - Dumplings ($4)"
                      "\n3 - Soup ($5)\n4 - No Appetizer\n"))
entree = int(input("Entree Options:\n1 - Cheeseburger ($12)\n2 - Personal Pizza ($14)"
                   "\n3 - Salmon ($22)\n"))
dessert = int(input("Dessert Options: \n1 - Ice Cream ($4)\n2 - Apple Pie ($6)"
                    "\n3 - Cheesecake ($8)\n4 - No Dessert\n"))
if drink == 1:
    drinkCost = 2
if drink == 2:
    drinkCost = 1.75
if drink == 3:
    drinkCost = 2.25
if drink == 4:
    drinkCost = 0

if appetizer == 1:
    appetizerCost = 7
if appetizer == 2:
    appetizerCost = 4
if appetizer == 3:
    appetizerCost = 5
if appetizer == 4:
    appetizerCost = 0

if entree == 1:
    entreeCost = 12
if entree == 2:
    entreeCost = 14
if entree == 3:
    entreeCost = 22

if dessert == 1:
    dessertCost = 4
if dessert == 2:
    dessertCost = 6
if dessert == 3:
    dessertCost = 8
if dessert == 4:
    dessertCost = 0

tip = int(input("Tip Selection: \n1 - 15%\n2 - 18%\n3 - 20%\n"))
if tip == 1:
    tipAmount = .15
if tip == 2:
    tipAmount = .18
if tip == 3:
    tipAmount = .2

mealCost = drinkCost + appetizerCost + entreeCost + dessertCost
tipCost = tipAmount * mealCost
taxCost = 0.07 * mealCost
totalCost = mealCost + tipCost + taxCost
print("Your meal cost a total of ${:.2f}! Come back soon!".format(totalCost))
