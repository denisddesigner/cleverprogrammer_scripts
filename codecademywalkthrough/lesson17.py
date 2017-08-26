from random import randint
# print battleship board

board = []

for _ in range(5):
		board.append(['O'] * 5)


def print_board(board_to_print):
	
		for row in board:
			print(" ".join(row))

print(print_board(board))


board2 = [

	['O','O','O','O','O'],
	['O','O','O','O','O'],
	['O','O','O','O','O'],
	['O','O','O','Hit','O'],
	['O','O','O','O','O'],

]


def print_board(board2):
	for row in board2:
		print(" ".join(row))

print_board(board2)


# LIST[row][col] --> the item you are looking for in a 2D list (GRID)

print(board2[3][3])



coin = randint(0, 1)
print(coin)
dice = randint(1, 6)
print(dice)








