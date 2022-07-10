from array import array
from ast import Lambda
import tkinter as tk


example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]





board = []
position_board = []

def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False # if we've repeated, then our guess is not valid!

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square
    row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)
    
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True 
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True
        
        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

#if __name__ == '__main__':


def make_puzzle(puzzle):
  for i in puzzle:
    position_board.append(i)
  
  create_board()
  make_board()



 
root = tk.Tk()

canvas = tk.Canvas(root, height=300, width=500)
canvas.pack()

background_image = tk.PhotoImage(file=r'C:\Users\laksh\Downloads\project\image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)


 
frame = tk.Frame(root)
frame.place(relx=0.1,rely=0.1,relwidth=0.6,relheight=0.8)

'''

entry= tk.Entry(frame)
entry.grid(row=1, column=2)
entry.insert(0,"you")
'''



#last step
def make_board():
  for i in range(0,9,1):
    for j in range(0,9,1):
      if position_board[i][j] != -1:
        string = str(position_board[i][j])

        board[9*i+j].delete(0)
        board[9*i+j].insert(0,string)



def create_board():
  for i in range(0,9,1):
    for j in range(0,9,1):
      entry= tk.Entry(frame, width=5)

      board.append(entry)
      board[-1].grid(row=i, column=j)



def update_box():
  for i in range(0,9,1):
    for j in range(0,9,1):
      if board[9*i+j].get() != "":
        position_board[i][j] = int(board[9*i+j].get())

def solve_board():

  print(solve_sudoku(position_board))
  make_board()








button = tk.Button(frame, text = "update board", command=lambda: update_box())
button.place(relx=0.5,rely=0.8,relwidth=0.3,relheight=0.2)

button2 = tk.Button(frame, text = "solve sudoku", command=lambda: solve_board())
button2.place(relx=0.1,rely=0.8,relwidth=0.3,relheight=0.2)


make_puzzle(example_board)



root.mainloop()
