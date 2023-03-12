import random
balance = 1000
while balance > 0:
  answer = random.randint(1, 2)
  maxBet = 1000
  if balance <= 1000:
    maxBet = balance
  bet = int(input("Enter a bet amount between 5 and {}: ".format(maxBet)))
# user will enter a bet amount between 1 to 1000
  if bet >= 5 and bet <= maxBet:
    guess = int(input("Choose between options 1 or 2: "))
# user will choose between options 1 and 2
    if guess == answer:
      balance += bet
    else:
      balance -= bet
    print("Balance: ", balance)
  else:
    print("Invalid bet. Please enter a bet amount between 5 and {}.".format(maxBet))
  if balance >= 5:
    choice = input("Do you want to continue? (yes/no)")
    if choice == "no":
      break
  else:
    print("You do not have enough money to continue. Game over.")
    break
print("Exit game, your balance is: ", balance)
# if the user enters no, then the statement on line 27 will be printed
