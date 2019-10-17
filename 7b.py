def print_board(board_size):
    for index in range(board_size):
        print(" --- " * (board_size-1))
        print("|    " * (board_size ))
    print(" --- " * (board_size-1))

board_size = int(input("What size of game board? "))

print_board(board_size)
    
