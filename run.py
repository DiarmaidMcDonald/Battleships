"""
Battleships Game Objective:

You try and hit the battleships by calling out the
coordinates of one of the squares on the board.  
Neither you nor the computer can see the other's board
so you must try to guess where they are.
You have 10 shots to sink all of your oppents battleships.

'X' represents a hit on players board.
'B' represents a battleship on computers board.

"""

import random

# Creating an empty board for the game board.
def create_board(size):
    return [['' for _ in range(size)] for _ in range(size)]

# Print the game board.
def print_board(board):
    for row in board:
        print(''.join(row))
    print('\nLet the Game Begin.\n')

# Put the computer's battleship randomly on the board for each game.
# 'B' represents a battleship.
def place_ships(board, num_ships):
    for _ in range(num_ships):
        while True:
            x = random.randint(0, len(board) - 1)
            y = random.randint(0, len(board) - 1)
            if board[y][x] == '':
                board[y][x] = 'B'
                break

# Users guess for the location of a battleship.
# Check if the guess is within the grid of the board.
def users_guess(board):
    while True:
        try:
            guess = input("Enter guess (row col): ")
            row, col = map(int, guess.split())
            if 0 <= row < len(board) and 0 <= col < len(board):
                return row, col
            else:
                print("Where are you off to? Try again.")
        except ValueError:
            print("Please enter numbers for the row and column.")

def main():
    user_score = 0
    computer_score = 0

    while True:
        board_size = 5
        num_ships = 4
        player_board = create_board(board_size)
        computer_board = create_board(board_size)
        print("Placing computer's battleships")
        place_ships(computer_board, num_ships)

        print("Welcome to Battleships")
        print("Take a guess on where the computer's Battleships are")
        print("You have 10 rockets, make them count!!")

        # User has 10 attempts to sink battleships
        attempts = 10
        while attempts > 0:
            print(f"Attempts left: {attempts}")
            print_board(player_board)
            row, col = users_guess(player_board)

            if computer_board[row][col] == 'B':
                print("Bingo, hit one!")
                player_board[row][col] = 'X'
                user_score += 1
            else:
                print("Dammit! I missed...")

            attempts -= 1

            # Check if all battleships are sunk.
            if all(cell == 'X' for row in player_board for cell in row):
                print("Bullseye, mission complete! Good job solider")
                break

        print("Game Over")
        print(f"Your Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        print("Computer's Battleships:")
        print_board(computer_board)

        play_again = input("Fancy another game? Yes/No:\n ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()