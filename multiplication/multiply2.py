def generate_multiplication_table(multiplier, times):
    # Print the welcome message
    print("Welcome to the Multiplication Table Generator!")
    # Get the user's name
    username = input("Please enter your name: ")
    # Print a greeting to the user
    print("Hello, {}! Let's generate a multiplication table.".format(username))
    # Get the number for which the user wants to generate a table
    number = int(input("Enter the number for which you want to generate the table: "))
    # Print a message confirming the number the user entered
    print("You have entered {}. Let's proceed.".format(number))

    # Loop through the range of 1 to the value of "times" + 1
    for i in range(1, times+1):
        # Calculate the product of the number and the current iteration
        product = number * i
        # Print the multiplication statement
        print("{} x {} = {}".format(i, number, product))

    # Print a thank you message to the user
    print("Thank you for using the Multiplication Table Generator, {}!".format(username))

# Call the function with the arguments multiplier=5, times=12
generate_multiplication_table(multiplier=5, times=12)
