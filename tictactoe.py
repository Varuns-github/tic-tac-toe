board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

def printBoard(board):
    print(" " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] + " ")
    print("---+---+---")
    print(" " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] + " ")
    print("---+---+---")
    print(" " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] + " ")
    print("\n")

def spaceIsFree(position):
    if(board[position] == " "):
        return True

    else:
        return False

def checkForWin():
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


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkIsDraw():
    for key in board.keys():
        if(board[key] == " "):
            return False
    return True


def insertInPosition(value, position, isBot = False):
    if(spaceIsFree(position)):
        board[position] = value
        print("\n")
        printBoard(board)
        if(checkIsDraw()):
            print("Neither of you won, its a draw")
            exit()
        if(checkForWin()):
            if(value == "X"):
                if(isBot):
                    print("Bot won the game fair and square")
                else:
                    print("X won the game fair and square")
                exit()
            else:
                print("O won the game fair and square")
                exit()

    else:
        print("Position is already occupied, please try another position \n")
        position = int(input("Enter new position:"))
        insertInPosition(value, position)
        return

def oPlayerMove(isBot = False):
    position = int(input("enter the position for O : "))
    insertInPosition("O", position)
    if(isBot):
        print("Bot move now, here comes the move")

def xPlayerMove():
    position = int(input("enter the position for X : "))
    insertInPosition("X", position)

def botMove():
    bestScore = -1000
    bestMove = 1

    for key in board.keys():
        if(board[key] == " "):
            board[key] = "X"
            score = minimax(board, 0, False)
            board[key] = " "
            if(score > bestScore):
                bestScore = score
                bestMove = key

    insertInPosition("X", bestMove, True)
    return

def minimax(board, depth, maximizing):

    if(checkWhichMarkWon("X")):
        return 1
    elif(checkWhichMarkWon("O")):
        return -1
    elif(checkIsDraw()):
        return 0

    if maximizing:
        bestScore = -1000

        for key in board.keys():
            if(board[key] == " "):
                board[key] = "X"
                score = minimax(board, 0, False)
                board[key] = " "
                if(score > bestScore):
                    bestScore = score

        return bestScore

    else:
        bestScore = 1000

        for key in board.keys():
            if(board[key] == " "):
                board[key] = "O"
                score = minimax(board, 0, True)
                board[key] = " "
                if(score < bestScore):
                    bestScore = score

        return bestScore

    

print("\n")
print("Welcome to Tic Tac Toe \n")
type = int(input("Please enter 1 if you want to play against a bot, enter 2 if you want to play with another person "))

if(type == 1):
    print("Bot move first, here comes the move \n")
    while not checkForWin():
        botMove()
        oPlayerMove(True)
else:
    print("Given below the board, please enter the position of O or X. Available positions are 1,2,3,4,5,6,7,8,9. \n")
    printBoard(board)
    while not checkForWin():
        xPlayerMove()
        oPlayerMove()

