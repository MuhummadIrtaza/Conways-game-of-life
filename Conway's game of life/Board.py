import random
import time
import copy
import os

class Board_logic:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def custom_board(self):
        #Getting the values from the .txt file custom
            dir_ = os.path.dirname(os.path.realpath(__file__)) + "/custom.txt"
            with open (dir_) as f:
                data = f.readlines()
        
        #making a new 2d array from the file
            data.remove("\n")
            new = []
            for row in data:
                r = []
                for cell in row:
                    if cell.isnumeric():
                        r.append(int(cell))
                    if cell == "\n":
                        new.append(r)
            return new
            

    def dead_state(self):
        board = [[0]* self.width for _ in range(self.height)]
        return board

    def random_board(self):
        board = self.dead_state()
        for rows in range(self.height):
            for cells in range(self.width):
                random_number = random.randint(0,1)
                board[rows][cells] = random_number
        return board


    def render(self, arr):
        for row in arr:
            for cell in row:
                if cell == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
            print("")
        


    def update(self, arr):
        new_arr = self.dead_state()
        for rows in range(self.height):
            for cells in range(self.width):
                new_arr[rows][cells] += self.check(arr, rows , cells)
        return(new_arr)


    def check(self, arr, x, y):
        m = 0 
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == j == 0) and (0 <= i+x < self.height) and (0 <= j+y < self.width):
                    m += arr[i+x][j+y]
        if arr[x][y]:
            if m == 2 or m == 3:
                return 1
        if not arr[x][y]:
            if m == 3:
                return 1
        return 0
    
    def run_simulation(self, arr):
        initial_state = arr
        while True:
            updated_state = self.update(initial_state)
            self.render(updated_state)
            initial_state = updated_state
            time.sleep(0.25)
            os.system('cls' if os.name == 'nt' else 'clear')








    

            
