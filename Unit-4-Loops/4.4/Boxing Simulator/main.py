"""
Author: Monish Mamilla
Program Name: Boxing Simulator
Date: 2/2/23
Version 1.0
"""
import random
replay = 1
while replay == 1:
    userHP = 100
    compHP = 100
    while userHP > 0 and compHP > 0:
        print("User HP:", userHP)
        print("Computer HP:", compHP)
        print("1. Block")
        print("2. Jab")
        print("3. Hook")
        print("4. Uppercut")
        print("5. Straight")
        choice = int(input("Choose your move: "))
# user will choose move
        compChoice = random.randint(1, 5)
        userDamage = 0
        userDefense = 0
        compDamage = 0
        compDefense = 0
        if choice == 1:
            userDamage = 0
            userDefense = random.randint(5, 10)
        elif choice == 2:
            userDamage = random.randint(1, 5)
            userDefense = random.randint(3, 5)
        elif choice == 3:
            userDamage = random.randint(3, 7)
            userDefense = random.randint(1, 3)
        elif choice == 4:
            userDamage = random.randint(4, 8)
            userDefense = random.randint(0, 2)
        elif choice == 5:
            userDamage = random.randint(2, 6)
            userDefense = random.randint(2, 4)
        else:
            print("You dropped your hands.")
        if compChoice == 1:
            compDamage = 0
            compDefense = random.randint(5, 10)
        elif compChoice == 2:
            compDamage = random.randint(1, 5)
            compDefense = random.randint(3, 5)
        elif compChoice == 3:
            compDamage = random.randint(3, 7)
            compDefense = random.randint(1, 3)
        elif compChoice == 4:
            compDamage = random.randint(4, 8)
            compDefense = random.randint(0, 2)
        elif compChoice == 5:
            compDamage = random.randint(2, 6)
            compDefense = random.randint(2, 4)
        print(compChoice)
        print("User Damage: {} | User Defense: {} | Comp Damage: {} | Computer Defense: {}"
              .format(userDamage, userDefense, compDamage, compDefense))
# damage, defense, comp damage, computer defense counter
        userChange = compDamage - userDefense
        compChange = userDamage - compDefense
        if userChange > 0:
            userHP -= userChange
        if compChange > 0:
            compHP -= compChange
    replay = int(input("Do you want to play again? (1 Yes / 2 No): "))
# asks the user whether they want to play again
