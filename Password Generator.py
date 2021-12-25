# Imports the random python class
import random

# Displays a welcome message to the user
print("Welcome to your own Password Generator")

# Creates chars array to hold the possible values for the password
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$$%^&*()-+_=.,?;0123456789"

# Displays message to the screen asking the user to enter the number of desired passwords they would like to generate
numberOfPasswords = input("Enter the number of passwords you would like to generate: ")
numberOfPasswords = int(numberOfPasswords)

# Displays message to the screen asking user to enter the number of desired characters to be in their passwords
lengthOfPasswords = input("Enter the number of characters you would like within your passwords: ")
# Converts the value of the lengthOfPasswords variable from string to integer
lengthOfPasswords = int(lengthOfPasswords)

# Displays message to the screen showing the new passwords
print("Here are your new passwords: ")

# Iterates through the passwords and randomizes the values within the password_chars array
for password in range(numberOfPasswords):
    passwords = ''
    for c in range(lengthOfPasswords):
        # Randomizes the passwords based on the contents of the password_chars array
        passwords += random.choice(password_chars)
    # Displays the newly generated passwords to the screen
    print(passwords)

# Displays a departure message to the user
print("Goodbye from your Password Generator!")