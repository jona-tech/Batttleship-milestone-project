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

