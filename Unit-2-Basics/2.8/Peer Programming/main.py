"""
Author: Monish Mamilla
Program: Peer Programming
Date: 11/9/22
"""
message = input("Enter a Message: ")
newMessage = message.upper()
newMessage = newMessage.replace("E", "3".replace("O", "0"))
print(message)
print(newMessage)

mes1 = input("Enter a word: ")
mes2 = input("Enter another word: ")
mes1Length = len(mes1)
mes2Length = len(mes2)
str1 = mes1[0]
str2 = mes2[0]
mes1 = mes1.replace(str1, str2)
mes2 = mes2.replace(str2, str1)
print(mes1)
print(mes2)
