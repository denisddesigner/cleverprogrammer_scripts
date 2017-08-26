import random

count = 0

while count < 10:
	print(count)
	count += 1



random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
	guess = int(input("Please enter your guess: "))
	if guess = random_number:
		print("You win")
	else:
		print("Sorry, you lose!")
		break
	guesses_left -= 1
