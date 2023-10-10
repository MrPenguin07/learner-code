# Welcome message
print("Welcome to the Multiplication Table Generator")

# Read username
username = input("Please enter your name: ")

# Accept input (multiplier) from user
multiplier = int(input("Please enter a number: "))

# Confirm user input
print("You have entered: " + str(multiplier))

# Process input
for i in range(1, 13):
    print(str(multiplier) + " x " + str(i) + " = " + str(multiplier * i))

# Display a “Thank you” message.
print("Thank you " + username + " for using the Multiplication Table Generator")