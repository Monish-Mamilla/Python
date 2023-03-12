# Get a number from the user
number = int(input("Enter a Number: "))

# Method 1 - A long Conditional
if number > 5 and number < 19 and number % 3 == 0:
    print("{} is in [6, 18] and divisible by 3!".format(number))

# Method 2 - Initialize a Boolean variable to hold True or False value
multiple3 = number > 5 and number < 19 and number % 3 == 0
# Use multiple 3 in conditional
if multiple3 == True:
    print("{} is in [6, 18] and divisible by 3!".format(number))

# Method 3 - You don't need to say == True
if multiple3:
    print("{} is in [6, 18] and divisible by 3!".format(number))

# Using not for the case where it's not a multiple of 3 in [6, 18]
if not multiple3:
    print("{} is not a multiple of 3 in [6, 18]!".format(number))
