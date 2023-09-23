board = [x + 1 for x in range(9)]


def print_board():
    print("\n")
    for row in range(3):
        print(f"{board[3*row]}|{board[3*row+1]}|{board[3*row+2]}")
        if row != 2:
            print("- - -")
    print("\n")


def valid_move(cell):
    return isinstance(board[cell - 1], int)


def check_win(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True


print("\nGAME HAS STARTED")
print_board()

player = "X"
while True:
    cell = int(input(f"Player {player}, your move:\n"))
    if valid_move(cell):
        board[cell - 1] = player
        if check_win(player):
            print(f"\nGame Over\nPlayer {player} won!!!\n\n")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("\nWrong Move")
    print_board()
