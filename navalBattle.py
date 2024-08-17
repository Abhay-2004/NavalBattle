# Abhay Prasanna Rao       11/21/22
# Assignment 6 - Naval Battle


import gameBoard
import gamePlay

def main():
    """This is the main function of the game. It controls the flow/ execution of the entire script.
    """
    gameOver = False

    gameboardChoice = 0
    humanGameBoard = None
    targetBoard = None
    computerGameBoard = None
    
    numHumanTargets = 0
    numComputerTargets = 0
    
    print("Welcome to Naval Battle!")
    print()

    print("By: Abhay Prasanna Rao ")
    print("[COM S 127 D]")
    print()

    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 

            gameboardChoice=gameBoard.chooseHumanGameBoard()
            pass

            humanGameBoard, numHumanTargets=gameBoard.loadGameBoard(gameboardChoice)
            pass

            gameboardChoice=gameBoard.chooseComputerGameBoard()
            pass


            computerGameBoard, numComputerTargets=gameBoard.loadGameBoard(gameboardChoice)
            pass

            targetBoard = gameBoard.loadTargetBoard()
            pass

            gamePlay.runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets)

        elif choice == "i":
            print("Enter a row and column to launch fire on the COMPUTER's ships!")
            print("To win: Sink all the COMPUTER's ships before the AI sinks yours!")
            print("To Loose : Let the AI sink your ships ! Hahah")
            pass
        elif choice == "q":
            gameOver=True
            print("Goodbye :) ")
            pass
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()