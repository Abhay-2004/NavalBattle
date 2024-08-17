# Abhay Prasanna Rao

import gameBoard
import gameInput

w=10
h=10

def _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets):
    """This function controls what happens when it is the human's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numComputerTargets (int): The number of computer targets remaining.
    
    Returns:
        list of lists, list of lists, list of lists, int: All of the relevant gameboards and the number of computer targets remaining.
    """


    print ("Human Turn")
    print("")
    gameBoard.printBoard(targetBoard, w, h)
    print("")
    gameBoard.printBoard(humanGameBoard, w, h)
    pass

    while True:
        row,col=gameInput.getHumanInput()
        pass

        print(f"The human targets coordinates ({row},{col})")

        pass

        if computerGameBoard[row][col]=="@":
            targetBoard[row][col]="X"
            computerGameBoard[row][col]="X"
            print ("HIT")
            numComputerTargets-=1
            break
        elif computerGameBoard[row][col]=="X":
            print("You have already attacked that spot. Pick a different spot.")

        elif computerGameBoard[row][col]=="O":
            print("You have already attacked that spot. Pick a different spot.") 
        else:
            computerGameBoard[row][col]="O"
            targetBoard[row][col]="O"
            print("MISS")
            break

    pass
    
    return humanGameBoard, targetBoard, computerGameBoard, numComputerTargets

def _computerTurn(humanGameBoard, numHumanTargets):
    """This function controls what happens when it is the computer's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets remaining.
    
    Returns:
        list of lists, int: All of the relevant gameboards and the number of human targets remaining.
    """


    print("Computer's Turn: ")
    pass

    while True:
        row,col=gameInput.getComputerInput()
        if humanGameBoard[row][col]!="X" or "O":
            break
        
    pass

    print(f"The Computer targets coordinates {row},{col}")

    pass


    if humanGameBoard[row][col]=="@":
        humanGameBoard[row][col]="X"
        print("HIT !")
        numHumanTargets-=1
    else:
        humanGameBoard[row][col]="O"
        print("MISS !")
    pass
    
    return humanGameBoard, numHumanTargets

def _printWinner(numComputerTargets, computerGameBoard):
    """This function prints out which player has won the game, depending on the numComputerTargets remaining.

    Args:
        numComputerTargets (int): The number of computer targets left. If there are none, the human wins. Else - the computer wins.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.
    """

    if numComputerTargets==0:
        print("Human has won !")
    else:
        print("Computer has won ! ")
    pass
    
    gameBoard.printBoard(computerGameBoard,w,h)

    pass

    return

def runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets):
    """This function controls the flow of the game and switches turns between the human and the computer.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets left.

        numComputerTargets (int): The number of computer targets left.
    """
    currentTurn = 0 # 0 = human, 1 = computer

    while numHumanTargets > 0 and numComputerTargets > 0:
        if currentTurn == 0:
            humanGameBoard, targetBoard, computerGameBoard, numComputerTargets = _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets)
        else:
            humanGameBoard, numHumanTargets = _computerTurn(humanGameBoard, numHumanTargets)


        currentTurn += 1
        currentTurn %= 2
    
    _printWinner(numComputerTargets, computerGameBoard)

    return