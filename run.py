from random import randint

# Create the board and ships list
board = [[' '] * 5 for x in range(5)]
ships = [[' '] * 5 for x in range(5)]


# Place the ships on the board at random locations
for i in range(5):
    r = randint(0, 4)
    c = randint(0, 4)
    ships[r][c] = 'S'


# Function to print the board
rows = 1
for row in board:
    print(rows, '|'.join(row))
    rows += 1


# Function to make move
def make_move(board, ships, col, row):
    if ships[col][row] == 'S':
        board[col][row] = 'X'
        print('Ouch! You HIT me!')
        return True
    else:
        board[col][row] = '-'
        print('Miss!!')
        return False

# Check if game over
def check_game_over(board, ships):
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ' and ships[i][j] == 'S':
                return False

def main():
    turns = 10
    while turns > 0:
        col, row = input('Choose column and row: ').split()
        col = int(col)
        row = int(row)


main()












