import random

board = ['a' for x in range(10)]

# function to insert a mark, either X or O, at a numbered location, num
def insertMark(mark, num):
    board[num] = mark

# checks if a certain space num is empty or not
def freeSpaceCheck(num):
    if board[num] == ' ':
        return True
    else:
        return False

# checks if the board has currently been filled
def boardFull():
    return board.count(' ') == 1

# prints the current state of the board
def printBoard():
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("-----------------------------------------------------")

# checks if there are any winners on the board
def checkBoard():
    return (board[1] == board[2] and board[2] == board[3] and (board[1] == 'X' or board[1] == 'O')) or (board[4]== board[5] and board[5] == board[6] and (board[4] == 'X' or board[4] == 'O')) or (board[7] == board[8] and board[8] == board[9] and (board[7] == 'X' or board[7] == 'O')) or (board[1] == board[5] and board[5] == board[9] and (board[1] == 'X' or board[1] == 'O')) or (board[3] == board[5] and board[5] == board[7] and (board[3] == 'X' or board[3] == 'O')) or (board[1] == board[4] and board[4] == board[7] and (board[1] == 'X' or board[1] == 'O')) or (board[2] == board[5] and board[5] == board[8] and (board[2] == 'X' or board[2] == 'O')) or (board[3] == board[6] and board[6] == board[9] and (board[3] == 'X' or board[3] == 'O'))

# resets the board
def resetBoard():
    for x in range(len(board)):
        board[x] = ' '

# basically just the printBoard function but with numbers at each location so that the players know where the numbers are
def printStartBoard():
    for x in range(len(board)):
        board[x] = str(x)
    printBoard()
    resetBoard()

# run one game
def runGame():
    run = True

    resetBoard()
    print("Welcome to Harbin's Tic-Tac-Toe Game")
    playerOne = str(input("What is player one's (X) name? "))
    playerTwo = str(input("What is player two's (O) name? "))
    print("-----------------------------------------------------")
    print("To decide who goes first, each player will pick one number between 0 and 9. Whoever is closest to a randomly picked unknown number will go first.")
    # the firstPlayer boolean will be true if playerOne is first and false if playerTwo is first
    firstPlayer = whoGoesFirst(playerOne, playerTwo)

    
    if(firstPlayer):
        printStartBoard()
        while(not checkBoard()):
            turn(playerOne, 'X')
            if(checkBoard()):
                print(playerOne + " won the game") 
                break
            if(boardFull()):
                print("No more moves available, tie game")
                break
            turn(playerTwo, 'O')
            if(checkBoard()):
                print(playerTwo + " won the game")
        
    else:
        printStartBoard()
        while(not checkBoard()):
            turn(playerTwo, 'O')
            if(checkBoard()):
                print(playerTwo + " won the game")
                break
            if(boardFull()):
                print("No more moves available, tie game")
                break
            turn(playerOne, 'X')
            if(checkBoard()):
                print(playerOne + " won the game") 


def turn(playerNum, mark):
    pos = int(input(playerNum + ", please pick a number 1-9 to mark a square on the board. "))
    print("-----------------------------------------------------")

    insertMark(mark, pos)
    printBoard()

    
def whoGoesFirst(playerOne, playerTwo):
    num = random.randint(0,9)
    p1Guess = abs(num - int(input("What is " + playerOne + "'s guess? ")))
    p2Guess = abs(num - int(input("What is " + playerTwo + "'s guess? ")))
    print("The number was " + str(num))
    if p1Guess < p2Guess:
        print(playerOne + " was closer. Congratulations, you will go first.")
        print("-----------------------------------------------------")
        return True
    else:
        print(playerTwo + " was closer. Congratulations, you will go first.")
        print("-----------------------------------------------------")
        return False
        
runGame()