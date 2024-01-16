#********************************Connect-4 Game********************************
import random
import os

ROW = 6
COL = 7

gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]
letters = ["A","B","C","D","E","F","G"]

def board():
    print("\tA\tB\tC\tD\tE\tF\tG", end="")
    for i in range(ROW):
        print("\n    +-------+-------+-------+-------+-------+-------+-------+")
        print(i, "  | \t", end="")
        for j in range(COL):
            if gameBoard[i][j] == "🔵":
                print("🔵 ", end=" |   ")
            elif gameBoard[i][j] == "🔴":
                print("🔴 ", end=" |   ")
            else:
                print("    |\t", end="")
    print("\n    +-------+-------+-------+-------+-------+-------+-------+")


def modifyArray(spacePicked, turn):
  gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
  #.........................................Check horizontal spaces.........................................
  for y in range(ROW):
    for x in range(COL - 3):
      if gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  #.........................................Check vertical spaces.........................................
  for x in range(ROW):
    for y in range(COL - 3):
      if gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  #............................Check upper right to bottom left diagonal spaces............................
  for x in range(ROW - 3):
    for y in range(3, COL):
      if gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip:
        print("\n",chip,"is winner!")
        return True

  #.............................Check upper left to bottom right diagonal spaces...........................
  for x in range(ROW - 3):
    for y in range(COL - 3):
      if gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip:
        print("\n",chip,"is winner!")
        return True
  return False

def coordinateParser(inputString):
  coordinate = [None] * 2
  if(inputString[0] == "A"):
    coordinate[1] = 0
  elif(inputString[0] == "B"):
    coordinate[1] = 1
  elif(inputString[0] == "C"):
    coordinate[1] = 2
  elif(inputString[0] == "D"):
    coordinate[1] = 3
  elif(inputString[0] == "E"):
    coordinate[1] = 4
  elif(inputString[0] == "F"):
    coordinate[1] = 5
  elif(inputString[0] == "G"):
    coordinate[1] = 6
  else:
    print("Invalid")
  coordinate[0] = int(inputString[1])
  return coordinate

def isSpaceAvailable(intendedCoordinate):
  if(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
    return False
  elif(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵'):
    return False
  else:
    return True

def gravityChecker(intendedCoordinate):
  #Calculate space below
  spaceBelow = [None] * 2
  spaceBelow[0] = intendedCoordinate[0] + 1
  spaceBelow[1] = intendedCoordinate[1]
  #Is the coordinate at ground level
  if(spaceBelow[0] == 6):
    return True
  #Check if there's a token below
  if(isSpaceAvailable(spaceBelow) == False):
    return True
  return False


#-----------------------------Function to clear the screen---------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

leaveLoop = False
turnCounter = 0
while(leaveLoop == False):
  clear_screen()
  if(turnCounter % 2 == 0):
    board()
    while True:
      spacePicked = input("\nChoose a space: ")
      coordinate = coordinateParser(spacePicked)
      try:
        #Check if the space is available
        if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
          modifyArray(coordinate, '🔵')
          break
        else:
          print("Not a valid coordinate")
      except:
        print("Error occured. Please try again.")
    winner = checkForWinner('🔵')
    turnCounter += 1
  #computers turn
  else:
    while True:
      cpuChoice = [random.choice(letters), random.randint(0,5)]
      cpuCoordinate = coordinateParser(cpuChoice)
      if(isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate)):
        modifyArray(cpuCoordinate, '🔴')
        break
    turnCounter += 1
    winner = checkForWinner('🔴')

  if(winner):
    board()
    break

