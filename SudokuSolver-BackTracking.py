print('''
 _____           _       _            _____       _                
/  ___|         | |     | |          /  ___|     | |               
\ `--. _   _  __| | ___ | | ___   _  \ `--.  ___ | |_   _____ _ __ 
 `--. \ | | |/ _` |/ _ \| |/ / | | |  `--. \/ _ \| \ \ / / _ \ '__|
/\__/ / |_| | (_| | (_) |   <| |_| | /\__/ / (_) | |\ V /  __/ |   
\____/ \__,_|\__,_|\___/|_|\_\\__,_| \____/ \___/|_| \_/ \___|_|   

Using Backtracking

By: MrLDGCA                                                                  
''')

# This program uses an exhaustive search method to solve the sudoku puzzle.
#   Every blank space is taken and the corresponding row, column and 3x3 cell is
#   is analysed to identify potential values. If only 1 value fits the space, it
#   is written to the space.
#   This process is repeated until no blank spaces remain.

'''
# Puzzle 01 : Easy
puzzle = [[2, 6, "-", "-", "-", "-", "-", "-", "-", ],
          ["-", 7, "-", "-", "-", 4, "-", 1, "-", ],
          [3, 5, "-", 6, 9, 1, 8, 7, "-", ],
          ["-", "-", 8, 2, "-", "-", "-", "-", "-", ],
          ["-", "-", 2, 5, 4, 6, 3, "-", "-", ],
          ["-", "-", "-", "-", "-", 9, 4, "-", "-", ],
          ["-", 2, 7, 9, 5, 3, "-", 4, 8, ],
          ["-", 4, "-", 7, "-", "-", "-", 9, "-", ],
          ["-", "-", "-", "-", "-", "-", "-", 5, 3]]

# Puzzle 02 : Hard
'''
puzzle = [["-", "-", "-", 8, 2, "-", "-", "-", 9],
          [4, 8, "-", 1, "-", "-", 2, "-", "-"],
          ["-", 9, "-", 6, "-", "-", "-", "-", "-"],
          ["-", 4, "-", "-", "-", "-", "-", "-", 5],
          [3, "-", 1, 2, "-", 5, 8, "-", 4],
          [5, "-", "-", "-", "-", "-", "-", 6, "-"],
          ["-", "-", "-", "-", "-", 2, "-", 1, "-"],
          ["-", "-", 4, "-", "-", 1, "-", 5, 6],
          [6, "-", "-", "-", 7, 8, "-", "-", "-"]]

'''
# Puzzle 03 : Hard
puzzle = [["-", "-", 5, 4, "-", 9, "-", "-", 1],
          ["-", "-", "-", "-", 7, "-", "-", 3, 6],
          ["-", 1, "-", "-", "-", "-", 4, "-", "-"],
          ["-", 5, 4, "-", "-", "-", "-", "-", "-", ],
          ["-", 3, "-", 6, 2, 8, "-", 5, "-"],
          ["-", "-", "-", "-", "-", "-", 3, 1, "-"],
          ["-", "-", 8, "-", "-", "-", "-", 2, "-"],
          [9, 7, "-", "-", 4, "-", "-", "-", "-", ],
          [3, "-", "-", 8, "-", 7, 6, "-", "-"]]
'''


def validatePuzzle():
    global spacesRemain
    for i, row in enumerate(puzzle):
        if len(row) != 9:
            print("Puzzle row #" + str(i + 1) + " is invalid !!!")
            spacesRemain = False
            return False
    if len(puzzle) != 9:
        print("Puzzle is invalid !!!")
        spacesRemain = False
        return False

    return True


def drawGrid():
    for row in range(9):
        if row % 3 == 0:
            print(" |---------|---------|---------|")
        for cell in range(3):
            print(" | " + str(puzzle[row][cell * 3 + 0]) + "  " + str(puzzle[row][cell * 3 + 1]) + "  " +
                  str(puzzle[row][cell * 3 + 2]), end="")
        print("")

    print(" |---------|---------|---------|")


def columnElements(index):
    elements = []
    for i in puzzle:
        elements.append(i[index])

    return elements


def cellElements(row, element):
    elements = []
    cellIndex = [row // 3, element // 3]
    for i in range(3):
        for j in range(3):
            n = puzzle[cellIndex[0] * 3 + i][cellIndex[1] * 3 + j]
            if n != "-":
                elements.append(n)
    return elements


def nextEmpty():
    for row in range(9):
        for index in range(9):
            if puzzle[row][index] == "-":
                return row, index
    return None


def solve():
    if nextEmpty() is None:
        return True
    else:
        row, index = nextEmpty()

    for i in range(1,10):
        if (i not in puzzle[row]) and (i not in columnElements(index)) and (i not in cellElements(row,index)):
            puzzle[row][index] = i

            if solve():
                return True

            puzzle[row][index] = "-"

    return False


# ======== main =========
if validatePuzzle():
    drawGrid()
    input("Start solving ?")

    solve()
    drawGrid()
    print("Did I get it?")

else:
    print("Fix the puzzle and try again")