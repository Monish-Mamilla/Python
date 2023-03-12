word = input("Enter a sentence: ")
counter = 0
numSpaces = 0
while counter < len(word):
    print(word[counter])
    if word[counter] == " ":
        numSpaces += 1
    counter += 1
else:
    print("Number of words: {}".format(numSpaces + 1))
