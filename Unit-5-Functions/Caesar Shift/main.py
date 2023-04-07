"""
Author: Monish Mamilla
Program Name: Caesar Shift
Date: 1/21/23
Version 1.0
"""
def caesar(text, key):
  length = len(text)
  caesarText = ''
  for x in range(length):
    letter = text[x]
    if ord(letter) >= 65 and ord(letter) <= 90:
      letter = chr(ord(letter) + key)
      if ord(letter) > 90:
        letter = chr(ord(letter) - 26)
      elif ord(letter) < 65:
        letter = chr(ord(letter) + 26)
    caesarText += letter
  print(caesarText)
text = input("Enter the text to be encrypted: ")
# user will enter the text that they want to encrypt
text = text.upper()
print("Unencrypted text: ", text)
# unencrypted text will be printed
key = int(input("Enter a value [0, 25]: "))
if key < 0 or key > 25:
  print("Key needs to be cured")
  if key < 0:
    key *= -1
    key %= 26
    key = 26 - key
  else:
    key %= 26
print("Cured key: ", key)
# Cured key will be printed
caesar(text, key)
# Unicode number will be printed
