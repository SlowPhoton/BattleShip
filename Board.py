
import os, sys

BOARD_SIZE = 10
X_LABEL = [1,2,3,4,5,6,7,8,9,10]
Y_LABEL = ['A','B','C','D','E','F','G','H','I','J']

class Board:
 
	def __init__(self):
		self.grid = [[0 for x in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]
#		self.grid[3][3] = 1
#		self.grid[5][7] = -1

	def clearScreen(self):
		os.system('clear')

	def printBoard(self):
		for i in range(len(self.grid)):
			if i == 0:
				print(' '),
				for z in X_LABEL:
					print(z),
				print
			for j in range(len(self.grid[i])):
				if j == 0:
					print(Y_LABEL[i]),
				if self.grid[i][j] == 0:
					# grid unknown
					print('.'),
				elif self.grid[i][j] == -1:
					# grid is a miss
					print('O'),
				elif self.grid[i][j] == 1:
					# grid is a hit
					print('X'),
			print

def main():
	board = Board()
	board.clearScreen()
	board.printBoard()

if __name__ == "__main__":
	main()
 
