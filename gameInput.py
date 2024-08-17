# Abhay Prasanna Rao

import random
import gameBoard

def getHumanInput():
    """This function takes in input from the human for wich row and column they want to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the human to attack.
    """
    while True:
        row=int(input("Enter the row to attack: "))
        if row <0 or row >gameBoard.GAME_BOARD_HEIGHT-1:
            print ("invalid input, try again.")
        else:
            break
    pass
    while True:
        col=int(input("Enter the column to attack: "))
        if col <0 or col >gameBoard.GAME_BOARD_WIDTH-1:
            print ("Invalid input....Try again !")
        else:
            break
    pass
    
    return row, col

def getComputerInput():
    """This function randomly generates input from the computer for which row and column it wants to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the computer to attack.
    """

    row=random.randint(0,gameBoard.GAME_BOARD_HEIGHT-1)
    pass

    col=random.randint(0,gameBoard.GAME_BOARD_WIDTH-1)
    pass

    return row, col