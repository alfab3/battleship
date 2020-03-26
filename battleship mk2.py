from random import randint

board = [] #Creating an empty guessboard
enemy_board = []

for x in range(10):
    enemy_board.append(["O"]*10)

for x in range(10):
    board.append(["O"]*10)
    
def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

print("Enemy Board")

def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board[0])-1)

def random_direction():
    return randint(0,1)

#AircraftCarrier
ac_ship_row = random_row(board)
ac_ship_col = random_col(board)
ac_direction = random_direction()
if ac_ship_row == 0:
    ac_ship_row = ac_ship_row + 2
elif ac_ship_row == 1:
    ac_ship_row = ac_ship_row + 1
elif ac_ship_row == 9: 
    ac_ship_row = ac_ship_row - 2
elif ac_ship_row == 8:
    ac_ship_row = ac_ship_row - 1

enemy_board[ac_ship_row][ac_ship_col] = "A"
if ac_direction == 1:
    enemy_board[ac_ship_row + 1][ac_ship_col] = "A"
    enemy_board[ac_ship_row + 2][ac_ship_col] = "A"
    enemy_board[ac_ship_row - 1][ac_ship_col] = "A"
    enemy_board[ac_ship_row - 2][ac_ship_col] = "A"
else:
    enemy_board[ac_ship_row][ac_ship_col + 1] = "A"
    enemy_board[ac_ship_row][ac_ship_col + 2] = "A"
    enemy_board[ac_ship_row][ac_ship_col - 1] = "A"
    enemy_board[ac_ship_row][ac_ship_col - 2] = "A"

#Battleship
bs_ship_row = random_row(board)
bs_ship_col = random_col(board)
bs_direction = random_direction()
if bs_ship_row == 0:
    bs_ship_row = bs_ship_row + 2
elif bs_ship_row == 1:
    bs_ship_row = bs_ship_row + 1
elif bs_ship_row == 9: 
    bs_ship_row = bs_ship_row - 2
elif bs_ship_row == 8:
    bs_ship_row = bs_ship_row - 1

enemy_board[bs_ship_row][bs_ship_col] = "B"
if bs_direction == 1:
    enemy_board[bs_ship_row + 1][bs_ship_col] = "B"
    enemy_board[bs_ship_row - 1][bs_ship_col] = "B"
    enemy_board[bs_ship_row - 2][bs_ship_col] = "B"
else:
    enemy_board[bs_ship_row][bs_ship_col + 1] = "B"
    enemy_board[bs_ship_row][bs_ship_col - 1] = "B"
    enemy_board[bs_ship_row][bs_ship_col - 2] = "B"

#Destroyer
    
#Submarine
    
#Patrol Boat

print_board(enemy_board)

print(ac_ship_row)
print(ac_ship_col)

for turn in range(4):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Column:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print ("Oops, thats not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already")
        else:
                print ("You missed my battleship!")
                board[guess_row][guess_col] = "X"
                if turn == 3:
                    print("Game Over")
                    
        print("Turn", turn + 1)
        print_board(board)