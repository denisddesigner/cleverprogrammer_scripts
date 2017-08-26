from random import randint

board = []

for x in range(0, 5):
	board.append(["O"] * 5)

def print_board(board):
	for row in board:
		print(" ".join(row))

print_board(board)

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board) - 1)



ship_row = random_row(board)
ship_col = random_col(board)


guesses = 0

while guesses < 4:
# user input
	guess_row = int(input('Guess Row: '))
	guess_col = int(input('Guess Col: '))


	# This checks if you guessed correctly
	if guess_row == ship_row and guess_col == ship_col:
		print("Congratulations! You sank my battleship!")
		break # or guesses = 4

	# This checks if you guessed within the 5x5 grid
	elif guess_row not in range(5) or guess_col not in range(5):
			print("Oops, that's not even in the ocean")

	# This checks if you arleady guessed in this location
	elif board[guess_row][guess_col] == 'X':
		print("You guessed that one already")


	# This tells you that you missed and marks spot with 'X'
	else: 
		print("You missed my battleship!")
		board[guess_row][guess_col] = 'X'
		print_board(board)
		guesses += 1
		if guesses == 4:
			print("Game Over!")
			print("Ship was at the following location:")
			print(ship_row)
			print(ship_col)




















