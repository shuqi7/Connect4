from cell import cell
import random
import tkinter as tk



board = []

# form a 6*7 board
for i in range(0,7):
    aList = []
    for j in range(0,6):
        aList.append(cell())
    board.append(aList)


#checkWin return true/false by checking if 4 points are same
def checkWin(p1, p2, p3, p4):
    if ((p1.color != "") and ((p1.color == p2.color) and ((p2.color == p3.color) and (p3.color == p4.color)))):
        return True
    else:
        return False



#check board to see if there is a win/lose/tie situation
def checkBoard():
    #check vertically
    for i in range(0, 7):
        for j in range(0,3):
            if checkWin(board[i][j], board[i][j+1], board[i][j+2], board[i][j+3]):
                return True

    #check horizontally
    for j in range(0, 6):
        for i in range(0, 4):
            if checkWin(board[i][j], board[i+1][j], board[i+2][j], board[i+3][j]):
                return True

    #check diagonally: 4 directions in total
    for i in range(0, 4):
        for j in range(0, 3):
            if checkWin(board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3]):
                return True

    for i in range(0, 4):
        for j in range(3, 6):
            if checkWin(board[i][j], board[i + 1][j - 1], board[i + 2][j - 2], board[i + 3][j - 3]):
                return True

    for i in range(3, 7):
        for j in range(0, 3):
            if checkWin(board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3]):
                return True

    for i in range(3, 7):
        for j in range(3, 6):
            if checkWin(board[i][j], board[i - 1][j - 1], board[i - 2][j - 2], board[i - 3][j - 3]):
                return True

    return False

# check if next move could be done
def movable(column):
    if column < 0 or column > 6:
        return False
    if board[column][5].color != "":
        return False
    else:
        return True

def move(column,x):
    for i in range(0, 6):
        if (board[column][i].color == ""):
            board[column][i].color = x
            break



def opponentMove():
    while True:
        next = random.randint(0,6)
        if movable(next):
            move(next, "blue")
            break



def textDisplay():
    for j in range(0, 6):
        j = 5 - j
        for i in range(0, 7):
            if board[i][j].color == "red":
                print("O", end=" ")
            elif board[i][j].color == "blue":
                print("X",end=" ")
            else:
                print ("-",end=" ")
        print("\n")



def makeMove(player, column):

    if bottom_circles[column] >= 6:
        return False # can't make move

    col = column
    row = bottom_circles[col]
    circle = circles[col][row]


    canvases[col].itemconfig(circle, fill=player)
    #change board

    board[col][row].color = player
    bottom_circles[col] += 1

    return True # move was OK


def onClick(event, number):
    global player

    # --- human ---

    player = 'red'

    column = number

    if not makeMove(player, column):
        print("Wrong move - full stack")
        return # skip computer move

    textDisplay()
    #check if human wins
    if checkBoard():
        print("You Win!")
        window.destroy();
        return

    #if sum(bottom_circles) == 7*6:
    if all(x == 6 for x in bottom_circles):
        print("Board is full")
        return # skip computer move

    # --- computer ---

    player = 'blue'

    while True:
        column = random.randint(0, 6)

        if not makeMove(player, column):
            print("Wrong move - full stack")
        else:
            break

    textDisplay()
    #check if computer wins
    if checkBoard():
        print("You Lose!")
        window.destroy();
        return

    #if sum(bottom_circles) == 7*6:
    if all(x == 6 for x in bottom_circles):
        print("Board is full")


# --- main ---

window = tk.Tk()
window.title("Connect 4")

player = 'blue'
bottom_circles = [0]*7

canvases = []
circles = []

for col in range(7):
    canvas = tk.Canvas(window, width=100, height=600, background='gray')
    canvas.grid(row=0, column=col)
    canvas.bind("<Button-1>", lambda event, number=col:onClick(event, number))

    canvases.append(canvas)

    circles_column = []
    for row in range(5, -1, -1):
        circle = canvas.create_oval(0, row*100, 100, (row+1)*100, fill="white")
        circles_column.append(circle)

    circles.append(circles_column)


def textMode():
    turn = 0
    while True:
        if turn == 0:
            turn += 1
            while True:
                while True:
                    nextMove = input("Enter a column you want to put the next piece: ")
                    try:
                        nextMove = int(nextMove)
                        break
                    except ValueError:
                        print("Please enter an integer from 1 to 7!")
                nextMove -= 1
                if (movable(nextMove)):
                    move(nextMove,"red")
                    textDisplay()
                    print("----------------")
                    if checkBoard():
                        print("You Win!")
                        return
                    break
                else:
                    print("Invalid move, please enter again")

        else:
            turn -= 1
            opponentMove()
            textDisplay()
            print("----------------")
            if checkBoard():
                print("You Lose!")
                return



