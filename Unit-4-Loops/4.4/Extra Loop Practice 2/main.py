"""
Author: Monish Mamilla
Program Name: Palindromes
Date: 2/14/23
Version 1.0
"""
message = input("Enter a message: ")
# Remove any spaces and convert to lowercase
message = message.replace(" ", "").lower()
# Use a for loop to check if the message is a palindrome
is_palindrome = True
for x in range(len(message)//2):
    if message[x] != message[-x-1]:
        is_palindrome = False
        break
# Print the result
if is_palindrome:
    print("The message is a palindrome!")
# if the user's message can be read the same way both times, then the message on line 18 will be printed
else:
    print("The message is not a palindrome.")
# if the user's message cannot be read the same way both times, then the message on line 21 will be printed
