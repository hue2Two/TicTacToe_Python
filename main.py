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

#check for win or tie (horizontal)
def checkHorizontal(board):
    global winner #implement change everywhere
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "_":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

#check for win or tie (vertical)
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True

#check for win or tie (diagonal)
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

#check for tie
def checkTie(board):
    if "_" not in board:
        printBoard(board)
        print("its a tie!")
        gameRunning = False

#switch the player

#game loop
while gameRunning:
    printBoard(board) #print the game board
    playerInput(board) #check the player input