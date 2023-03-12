"""
Author: Monish Mamilla
Program Name: Extra Loop Practice 3
Date: 2/13/23
Version 1.0
"""
message = input("Enter a message: ")
# user will enter a message
vowels = 0
consonants = 0
numbers = 0
spaces = 0
special_chars = 0
# initial value of all variables
for char in message:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
# if "aeiou" is part of the message, then the vowels counter will increase
        else:
            consonants += 1
# if any other letter is in the message, then the consonants counter will increase
    elif char.isdigit():
        numbers += 1
    elif char.isspace():
        spaces += 1
    else:
        special_chars += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Numbers:", numbers)
print("Spaces:", spaces)
print("Special Characters:", special_chars)
# after the message, the count for Vowels, Consonants, Numbers, Spaces, and Special Characters will be added
