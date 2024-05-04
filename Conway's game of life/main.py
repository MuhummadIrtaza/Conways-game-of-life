import time
import os
from Board import Board_logic


def gamemode(): 
    dir_ = os.path.dirname(os.path.realpath(__file__)) + "/art.txt"
    with open (dir_) as f:
        data = f.read()
        print(data , end="")

    while True:
        print("Which game mode do you want to play?")
        gm = input("1. Random , 2.Custom: ")
        if gm.isnumeric and gm == "1" or gm == "2":
            return(gm)
        else:
            print("Wrong input enter 1 or 2 \n")
    

if __name__ == "__main__":
    board = Board_logic

    #random game mode
    if gamemode() == "1":
        height = input("Please enter the height: ")
        width = input("Please enter the width: ")

        board = board(int(height), int(width))
        random = board.random_board()
        board.run_simulation(random)

    #Custom game mode
    else:
        board = board(6,6)
        x1 = board.custom_board()
        board.run_simulation(x1)

