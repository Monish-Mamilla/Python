"""
Author: Monish Mamilla
Program Name: Pythagorean Theorem
"""
# Define the function to decrypt a Caesar Cipher
def decrypt(text):
    # Get the length of the text string
    length = len(text)
    # Initialize the unencrypted string to empty
    unencrypt = ''
    # Loop through each character in the text string
    for counter in range(length):
        # Get the current character
        letter = text[counter]
        # Check if the character is a letter (A-Z)
        if ord(letter) in range(65, 91):
            # Shift the letter by one (Caesar Cipher)
            letter = chr((ord(letter) - 65 + 25) % 26 + 65)
            # Concatenate the unencrypted letter to the result string
            unencrypt += letter
    # Return the unencrypted string
    return unencrypt
# Main program
# Prompt the user to enter the encrypted text
text = input("Enter a encrypted message: ")
# Convert the text to all uppercase letters
text = text.upper()
# Initialize the key to 26 (the maximum possible shift)
key = 26
# Initialize the decrypted message to the encrypted text
dec = text
# Initialize the choice to 1 (continue trying keys)
choice = 1
# Loop until the user chooses to stop
while choice == 1:
    # Decrypt the message with the current key
    dec = decrypt(dec)
    # Subtract 1 from the key for the next decryption attempt
    key -= 1
    # Print the current key and the decrypted message
    print("Key:", key, "Decrypted message:", dec)
    # Prompt the user to choose the next action
    choice = int(input("Enter 1 to try the next key, or 2 to stop: "))
# Print the final decrypted message and the key used to encrypt it
print("Final decrypted message:", dec)
print("Key used to encrypt the message:", 26 - key)
