from random import randint

#ship class
class ship(object):
	#ship's position
	row = 0
	col = 0
	ship_name = ""
	
	
	#initialize ship object with 
	#row and col args
	def __init__(self, ship_name, row, column):
		self.row = row
		self.col = column
		self.ship_name = ship_name
	

	def get_row(self):
		return self.row
	
	def get_col(self):
		return self.col

	def get_ship_name(self):
		return self.ship_name

	def ship_position(self):
		print("[" + str(self.row) + "," + str(self.col) + "]")
		

board = [] #gameboard

#create 5x5 grid
for x in range(5):
  board.append(["O"] * 5)

#method to print out game board
def print_board(board):
  for row in board:
		#join() used to remove quotations
    print(" ".join(row))

print_board(board)

#generate ship's random row value
def random_row(board):
  return randint(0, len(board) - 1)
#generate ships's random col value
def random_col(board):
  return randint(0, len(board[0]) - 1)

#create enemy ships
battleship = ship("Battleship", random_row(board), random_col(board))
destroyer = ship("Destroyer", random_row(board), random_col(board))
cruiser = ship("Cruiser", random_row(board), random_col(board))

print(type(battleship.get_ship_name()))
battleship.ship_position()
destroyer.ship_position()
cruiser.ship_position()

#Begin the game
turn = 1

while turn <= 4:
	print("Turn " + str(turn))

	#get player guess
	guess_row = int(input("Guess Row: "))
	guess_col = int(input("Guess Column: "))

	#check player guess
	#battleship
	if guess_row == battleship.get_row() and guess_col == battleship.get_col():
		print("Congratulations! You sunk my %s." % battleship.get_ship_name())
		board[guess_row][guess_col] = "S"
	#destroyer
	elif guess_row == destroyer.get_row() and guess_col == destroyer.get_col():
		print("Congratulations! You sunk my %s." % destroyer.get_ship_name())
		board[guess_row][guess_col] = "S"
	#cruiser
	elif guess_row == cruiser.get_row() and guess_col == cruiser.get_col():
		print("Congratulations! You sunk my %s." % cruiser.get_ship_name())
		board[guess_row][guess_col] = "S"
	else:
		 #player guessed incorrectly
		 if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			 print("Oops, that's not even in the ocean.")
		 elif (board[guess_row][guess_col] == "X"):
			 print("You guessed that one already.")
		 else:
			 print("You missed my battleship!")
			 board[guess_row][guess_col] = "X"

		 if turn == 4:
			 print("Game Over!")

	#show player the board and update turn by 1
	print_board(board)
	turn += 1		
