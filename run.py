import random

# Creating an empty board for game board.

def create_board(size):
    return [['' for _ in range(size)] for _ in range(size)]

# Print the game board.

def print_board(board):
    for row in board:
        print(''.join(row))
        print('Let the Game Begin')

# Put the computers battleship randomly on the board for each game.
# 'B' is a battleship.

def place_ships(board, num_ships):
    for i in range(num_ships):
        while True:
            x = random.randint(0, len(board) -1)
            y = random.randint(0, len(board) -1)
            if board[y][x] = '':
                board[y][x] = 'B'
                break

