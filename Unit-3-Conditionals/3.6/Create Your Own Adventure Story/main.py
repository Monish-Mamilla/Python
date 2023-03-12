"""
Author: Monish Mamilla
Program Name: Create Your Own Adventure Story
Date: 11/19/22
"""
choice1 = "You are on a mission to rescue a princess from a dinosaur.\nShe is very faraway, are you going to.\n1. Ask for help\n2. Look in her house for her whereabouts\n3. Forget about it so that you can enjoy the rest of your day\n"
choice1res1 = "You scream out for help and meet a man who says that he saw her going South."
choice1res2 = "You go to her house and you look at her calendar which says that she has a doctor's appointment today."
choice1res3 = "Once you realize that the princess neither treated you properly or cared about your well being, you go on a train back home."

choice2 = "\n\nYou remember that you gave the princess your wallet.\nDo you:\n1. Leave wherever you are and sprint to find her\n2. Continue at the same pace\n3. Not care so that you can continue your day\n"
choice2res1 = "You realize that she has your wallet, therefore, you sprint to where you believe she is, however you meet someone who demands money\nDo you\n1. Push him aside and continue\n2. Reason with him and ask him to join you."
choice2res2 = "You keep going hoping to find the princess and attain riches from her such as gold or money."
choice2res3 = "You continue along and miraculously find the princess and the dinosaur. However, the door is blocked by two guards."

choice3 = "\n\nDo you:\n1. Run and Hide\n2. Fight them."
choice4 = "\n\nYou fight the guards and beat them up. You find the dinosaur and the princess.\nDo you\n1. Kick the door open\n2. Come back later to get the princess\n3. Disguise as a guard to come inside.\n"

decision = "You kick the door open and the fight the dinosaur. The dinosaur gives you a black eyes and breaks your arm, but your still able to defeat him and rescue the princess."

anotherdecision = "You disguise yourself as a guard and knock on the door. The dinosaur realizes you are an impostor so he destroys you."
#entire story and the user chooses between the options above
print(choice1)
#choice variable and first prompt
choice = int(input("What do you choose? "))
if (choice == 1 or choice == 2):
	if choice == 1:
		print(choice1res1)
	else:
		print(choice1res2)
	#2nd choice
	print(choice2)
	choice = int(input("What do you choose? "))
	if choice == 1:
		print(choice2res1)
		choice = int(input("What do you choose? "))
		if choice == 1:
				print(choice2res3)
			#elif choice
		elif choice == 2:
			print(choice2res2)
			print(choice3)
			choice = int(input("What do you choose? "))
			if choice == 1:
				#win
				print(decision)
			elif choice == 2:
				print(anotherdecision)
	elif choice == 2:
		print(choice2res2)
		print("Do you\n1. Approach the door quietly\n2. Try and kick the door down")
		choice = int(input("What do you choose? "))
		if choice == 1:
			print(choice4)
			choice = int(input("What do you choose? "))
			if choice == 1:
				print(choice2res3)
			elif choice == 2:
				print(decision)
			elif choice == 3:
				print(anotherdecision)
	elif choice == 3:
		print(choice2res3)
else:
	print(choice1res3)
