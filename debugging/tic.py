#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the game board.

    Parameters:
    board (list of list of str): The 3x3 game board where each element is 'X', 'O', or ' '.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner in the game.

    Parameters:
    board (list of list of str): The 3x3 game board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows and columns for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Check if the board is full (no empty spots left).

    Parameters:
    board (list of list of str): The 3x3 game board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    
    Description:
    This function initializes the game board and alternates between players 'X' and 'O' to place their marks.
    The game continues until there is a winner or the board is full, at which point it ends and announces the result.
    
    Parameters:
    None

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            # Check if the input is within the valid range
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter values between 0 and 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("The game is a draw!")
                    break
                # Switch player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    tic_tac_toe()
