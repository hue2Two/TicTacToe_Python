#project: tictactoe in python

#print the game board
#take player input
#check for win or tie
#switch the player
#check for win or tie again

#global vars
board = [
    "_", "_", "_",
    "_", "_", "_",
    "_", "_", "_",
]
currentPlayer = "X"
winner = None
gameRunning = True #to control game loop

#to print gameboard
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#take player input
def playerInput(board):
    inp = int(input("enter a number 1-9: ")) #input

    #check if input is valid
    if inp >= 1 and inp <= 9 and board[inp-1] == "_":
        board[inp - 1] = currentPlayer
    else:
        print("oops player is already in that spot")

#game loop
while gameRunning:
    printBoard(board) #print the game board
    playerInput(board) #check the player input