board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

player = '0'
computer = 'X'

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

# printBoard(board)

#if there is a space to go to
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

#inserting a letter at a point in the board
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

        if checkDraw():
            print("Draw!")
            exit()
        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("invalid position")
        position = int(input("please enter a new position: "))
        insertLetter(letter, position) #recursive
        return

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
        return True

def playerMove():
    position = int(input("enter a postion for 0"))
    insertLetter(player, position)
    return

def compMove():
    position = int(input("enter a postion for X"))
    insertLetter(computer, position)
    return

while not checkWin():
    compMove()
    playerMove()