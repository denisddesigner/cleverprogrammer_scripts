from random import randint

board = []

for x in range(0, 5):
	board.append(["O"] * 5)

print(board)

print('\n\n')
# Place hidden item
random_row = randint(0, len(board) - 1)
random_col = randint(0, len(board) - 1)


board[random_row][random_col] = 'HIDDEN'

print(board)