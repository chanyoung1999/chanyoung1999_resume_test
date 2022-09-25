'''Tic-Tac-Toe: A Solution 
Author: ChanYoung Choi
'''

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(25):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}|{board[3]}")
    print('-+-+-+-')
    print(f"{board[4]}|{board[5]}|{board[6]}|{board[7]}")
    print('-+-+-+-')
    print(f"{board[8]}|{board[9]}|{board[10]}|{board[11]}")
    print('-+-+-+-')
    print(f"{board[12]}|{board[13]}|{board[14]}|{board[15]}")
    print('-+-+-+-')

    
def is_a_draw(board):
    for square in range(25):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] == board[3] or
            board[4] == board[5] == board[6] == board[7] or
            board[8] == board[9] == board[10] == board[11] or
            board[12] == board[13] == board[14] == board[15] or
            board[1] == board[4] == board[7] == board[3] or
            board[2] == board[5] == board[8] == board[3] or
            board[0] == board[4] == board[8] == board[3] or
            board[2] == board[4] == board[6] == board[3])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()