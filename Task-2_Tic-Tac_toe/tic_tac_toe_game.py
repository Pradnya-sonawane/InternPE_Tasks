from random import randint
from ttt import text
import os


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player = 'X'
winner = None
gamerunning = True


def board_printing(b):
    for i in range(len(b)):
        if (i+1) %3 ==0 and i!=8:
            print(f"\t{b[i]} \n\t-------------------")
        elif i!=8:
            print(end=f"\t{b[i]}   |  ")
        else:
            print(f"\t{b[i]}")


def user_input(b):
    n = int(input("Enter number 1-9 : "))
    if n > 0 and n <= 9 and b[n-1] == "-":
        b[n-1] = player
    else:
        print("Position is already occupied!")


#-------------------------------check for win or tie ----------------------------
def horizontal_win(b):
    global winner
    for i in range(0, 9, 3):
        if b[i] == b[i+1] == b[i+2] and b[i] != "-":
            winner = b[i]
            return True

def vertical_win(b):
    global winner
    for i in range(0, 3, 1):
        if b[i] == b[i+3] == b[i+6] and  b[i] != "-":
            winner = b[i]
            return True

def diagonal_win(b):
    global winner
    if b[0] == b[4] == b[8] and  b[0] != "-":
        winner = b[0]
        return True
    elif b[2] == b[4] == b[6] and  b[0] != "-":
        winner = b[2]
        return True

def Tie(b):
    global gamerunning
    if "-" not in b:
        print("It's a Tie!")
        board_printing(board)
        gamerunning = False

def win():
    global gamerunning
    if horizontal_win(board) or vertical_win(board) or diagonal_win(board):
        print(f"player {winner} is winner!")
        board_printing(board)
        gamerunning = False
        return True
    return False

#----------------------------------switch the player------------------------------------

def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

#---------------------------------------Computer----------------------------------------
        
def computer(b):
    while player == "O":
        pos = randint(0,8)
        if b[pos] == "-":
            b[pos] = "O"
            switch_player()


# =-----------------------------Function to clear the screen---------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



while gamerunning:
    clear_screen()
    print(text)
    board_printing(board)
    user_input(board)
    if win():
        break

    Tie(board)
    switch_player()

    if gamerunning:
        computer(board)
        if win():
            break

        Tie(board)
    

