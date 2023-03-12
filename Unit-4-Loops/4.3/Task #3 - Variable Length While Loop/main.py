# Create a variable to store the sum of the numbers entered
total = 0
# Create a list to store the numbers entered
numbers = []
while True:
    # Ask the user to enter a number
    number = int(input("Enter a number (0 to stop): "))
    # Check if the user entered 0 to stop
    if number == 0:
        # If the user entered 0, break out of the loop
        break
    # Add the number to the total
    total += number
    # Append the number to the numbers list
    numbers.append(number)
# Calculate the average of the numbers entered
average = total / len(numbers)
# Print out the numbers entered and the average
print("The average of", numbers,"is", average)
