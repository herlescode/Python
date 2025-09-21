import random

# Set the secret_number variable here (between 1 and 10)
secret_number = 7

# Initialize the guess variable here with a value of 0
guess = 0

while guess != secret_number:# Add the while loop condition here
	guess = random.randint(1, 10)
	print("Guessing:",guess)

print("I guessed the right number! It was",secret_number)