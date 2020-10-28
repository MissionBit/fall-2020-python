# Tic Tac Toe

board = [[" "]*3 for i in range(3)]
gameOver = False
personTurn = True
winner = ""

def print_board(player):
    print(player + " move:")
    print(" | ".join(board[0]))
    print("---------")
    print(" | ".join(board[1]))
    print("---------")
    print(" | ".join(board[2]))
    print()
    print()

def gameWon():
    if board[0][0] != " " and board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return True
    if board[1][0] != " " and board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return True
    if board[2][0] != " " and board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return True
    if board[0][0] != " " and board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return True
    if board[0][1] != " " and board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True
    if board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    return False


def person_move():
    moveOver = False
    move = input("Please input the position you would like to make your move. ")
    while moveOver == False:
        if(move == "Top Left"):
            if(board[0][0] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[0][0] = "X"
                moveOver = True
        elif (move == "Middle Left"):
            if (board[1][0] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[1][0] = "X"
                moveOver = True
        elif (move == "Bottom Left"):
            if (board[2][0] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[2][0] = "X"
                moveOver = True
        elif (move == "Top Middle"):
            if (board[0][1] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[0][1] = "X"
                moveOver = True
        elif (move == "Exact Middle"):
            if (board[1][1] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[1][1] = "X"
                moveOver = True
        elif (move == "Bottom Middle"):
            if (board[2][1] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[2][1] = "X"
                moveOver = True
        elif (move == "Top Right"):
            if (board[0][2] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[0][2] = "X"
                moveOver = True
        elif (move == "Middle Right"):
            if (board[1][2] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[1][2] = "X"
                moveOver = True
        elif (move == "Bottom Right"):
            if (board[2][2] != " "):
                input("That space is already full. Please choose another one.")
            else:
                board[2][2] = "X"
                moveOver = True
        else:
            move = input("Invalid space. Please try again with a valid space. Ex: 'Middle Left' ")
    print_board("Your")
    return gameWon()


def computer_move():
    moveOver = False
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == "O" and board[i-1][j] == " ":
                board[i-1][j] = "O"
                moveOver = True
                break;
            if board[i][j] == "O" and board[i][j-1] == " ":
                board[i][j-1] = "O"
                moveOver = True
                break;
        if moveOver == True:
            break;

    if moveOver == False:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    moveOver = True
                    break;
                if board[i][j] == " ":
                    board[i][j - 1] = "O"
                    moveOver = True
                    break;
            if moveOver == True:
                break;
    print_board("Computer")
    return gameWon()



while gameOver == False:
    if personTurn == True:
        gameOver = person_move()
        personTurn = False
    else:
        gameOver = computer_move()
        personTurn = True
if personTurn == True:
    winner = "Computer"
else:
    winner = "Person"
print("Game over! " + winner + " is the winner.")



