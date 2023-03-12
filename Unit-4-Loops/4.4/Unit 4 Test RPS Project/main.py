import random
# define a function so it can be called later, I learned this by going ahead to 4.5
# essentially, you define a function first and then you can call it in any other function or on its own for example, I could print on a blank line with no indentations, (def rps_single_game())
def rps_single_game():
  # ask user_choice and input string values for the numbers that the user entered
    user_choice = int(input("Pick: \n1 - Rock\n2 - Paper\n3 - Scissors\n"))
    if user_choice == 1 or user_choice == 2 or user_choice == 3:
      if user_choice == 1:
        user = "Rock"
      elif user_choice == 2:
        user = "Paper"
      elif user_choice == 3:
        user = "Scissors"
      # set random string values for computer choice and input interger values for each string
      computer_choice = random.choice(["Rock", "Paper", "Scissors"])
      if computer_choice == "Rock":
          computer = 1
      elif computer_choice == "Paper":
        computer = 2
      elif computer_choice == "Scissors":
        computer = 3
      # print the computer choice and the user choice in string form
      print("Computer chose:", computer_choice)
      print("You chose: ", user)
      # set if,elif, else chain to check for draw, user win, or computer win
      if user_choice == computer:
        print("It's a draw. Let's play again.")
      elif user_choice == 1 and computer_choice == "Scissors":
        print("You win!")
      elif user_choice == 2 and computer_choice == "Rock":
        print("You win!")
      elif user_choice == 3 and computer_choice == "Paper":
        print("You win!")
      else:
        print("CPU WINS!")
    # else statement if user fails to enter 1, 2, or 3
    else:
      print("Invalid option. Please enter 1, 2, or 3!")
    # recall function game_menu() so the user has options again
    game_menu()

import random
# define a function so it can be called later, I learned this by going ahead to 4.5
# essentially, you define a function first and then you can call it in any other function or on its own for example, I could print on a blank line with no indentations, (def rps_single_game())
def rps_single_game():
  # ask user_choice and input string values for the numbers that the user entered
    user_choice = int(input("Pick: \n1 - Rock\n2 - Paper\n3 - Scissors\n"))
    if user_choice == 1 or user_choice == 2 or user_choice == 3:
      if user_choice == 1:
        user = "Rock"
      elif user_choice == 2:
        user = "Paper"
      elif user_choice == 3:
        user = "Scissors"
      # set random string values for computer choice and input interger values for each string
      computer_choice = random.choice(["Rock", "Paper", "Scissors"])
      if computer_choice == "Rock":
          computer = 1
      elif computer_choice == "Paper":
        computer = 2
      elif computer_choice == "Scissors":
        computer = 3
      # print the computer choice and the user choice in string form
      print("Computer chose:", computer_choice)
      print("You chose: ", user)
      # set if,elif, else chain to check for draw, user win, or computer win
      if user_choice == computer:
        print("It's a draw. Let's play again.")
      elif user_choice == 1 and computer_choice == "Scissors":
        print("You win!")
      elif user_choice == 2 and computer_choice == "Rock":
        print("You win!")
      elif user_choice == 3 and computer_choice == "Paper":
        print("You win!")
      else:
        print("CPU WINS!")
    # else statement if user fails to enter 1, 2, or 3
    else:
      print("Invalid option. Please enter 1, 2, or 3!")
    # recall function game_menu() so the user has options again
    game_menu()

