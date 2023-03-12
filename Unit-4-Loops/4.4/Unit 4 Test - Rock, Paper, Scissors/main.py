"""
Author: Monish Mamilla
Program Name: Unit 4 Test - Rock, Paper, Scissors
Date: 2/6/23
Version 1.0
"""
import random
def play_single_game():
    options = ["Rock", "Paper", "Scissors"]
    user_choice = input("Pick Rock, Paper, or Scissors: ")
    computer_choice = random.choice(options)
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    while user_choice == computer_choice:
        print("It's a draw. Keep Playing.")
# if the user and the computer enter the same choice, then line 15 will be printed
        user_choice = input("Pick Rock, Paper, or Scissors: ")
        computer_choice = random.choice(options)
        print("Computer chose:", computer_choice)
    if (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("Computer wins!")
def play_series_of_games():
    options = ["Rock", "Paper", "Scissors"]
    number_of_games = int(input("Enter an odd number of games to play: "))
# user will have to enter an odd number to play
    if number_of_games == 1:
        print('You should have chosen that option last question!')
        return
    if number_of_games % 2 == 0:
        print("Invalid output, number must be odd.")
        return
    if number_of_games < 0:
        print("Invalid output, number must be positive.")
# if the user enters 1, a negative number, or an even number, then line 29, 32, or 35 will be printed
        return
    user_score = 0
    computer_score = 0
    target_score = number_of_games // 2 + 1
# whoever wins the majority of the rounds in the series, will be the winner
    for x in range(number_of_games):
        user_choice = input("Pick Rock, Paper, or Scissors: ")
        computer_choice = random.choice(options)
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        if user_choice == computer_choice:
            print("It's a draw.")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
            user_score += 1
            print("You win this round.")
# each time the user wins, they will receive a point
        else:
            computer_score += 1
# each time the user wins, they will receive a point
            print("Computer wins this round.")
        print("Score: You", user_score, "|", "Computer", computer_score)
        if user_score == target_score:
            print("You won the series!")
            break
        elif computer_score == target_score:
            print("Computer won the series.")
            break
def quit_program():
    print("Goodbye!")
# if the user chooses option 3: quit, then the goodbye message will be printed
while True:
    print("Choose an option:")
    print("1. Play a single game")
    print("2. Play a series of games")
    print("3. Quit")
    choice = int(input("Enter your choice (1, 2, or 3): "))
# user has to enter 1,2, or 3 to start playing the game
    if choice == 1:
        play_single_game()
    elif choice == 2:
        play_series_of_games()
    elif choice == 3:
        quit_program()
        break
    else:
        print("Invalid choice, try again.")
# if the user doesn't enter 1, 2, or 3 then line 82 will be printed
