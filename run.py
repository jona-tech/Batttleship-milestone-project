from random import randint

# Create the board and ships list
board = [[' '] * 5 for x in range(5)]
ships = [[' '] * 5 for x in range(5)]


# Place the ships on the board at random locations
for i in range(5):
    r = randint(0, 4)
    c = randint(0, 4)
    ships[r][c] = 'S'


def print_board(board):
    """
    Function to print the board
    """
    print('- - - - - -\nBATTLESHIPS\n- - - - - -\n  1 2 3 4 5')
    rows = 1
    for row in board:
        print(rows, '|'.join(row))
        rows += 1


def make_move(board, ships, col, row):
    """
    Function to make move
    """
    if ships[col][row] == 'S':
        board[col][row] = 'X'
        print('Ouch! You HIT me!')
        return True
    else:
        board[col][row] = '-'
        print('Miss!!')
        return False


def check_move(board, col, row):
    """
    Check if move is valid
    """
    if col < 0 or col > 4 or row < 0 or row > 4:
        return False
    if board[col][row] == ' ':
        return True
    return False


def check_game_over(board, ships):
    """
    Check if game over
    """
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ' and ships[i][j] == 'S':
                return False


def main():
    """
    Main function for gameplay
    """
    turns = 10
    print_board(board)
    while turns > 0:
        try:
            col, row = input('Choose column and row: \n').split(',')
            col = int(col)-1
            row = int(row)-1
        except ValueError:
            print('Invalid input! \nFormat should be two numbers between 1-5, \
                separated by a comma.\n ')
            continue

        if not check_move(board, col, row):
            print('Move invalid or out of range!')
            continue

        if make_move(board, ships, col, row):
            if check_game_over(board, ships):
                print('You win!')
                break
        else:
            if check_game_over(board, ships):
                print('Game over!')
                break

        turns -= 1
        print_board(board)


# Print welcome and information
print('Welcome to Battleships game!')
print('\n\nInfo:\nThere are five ships hiding on the game-board\
    \nYour mission is to hit all five ships before your ten rounds are over\
    \nYou have to pick a row and a column to make a move')
print('The format should be "column, row".\nExample: 2, 5')
# Start game
main()
