def is_valid_sudoku():
    print("Enter the Sudoku grid row by row (use '.' for empty cells):")
    board = [input().split() for _ in range(9)]

    def is_valid_block(block):
        block = [x for x in block if x != '.']
        return len(block) == len(set(block))

    for i in range(9):
        if not is_valid_block(board[i]):
            print("Invalid Sudoku: Row issue.")
            return
        if not is_valid_block([board[j][i] for j in range(9)]):
            print("Invalid Sudoku: Column issue.")
            return

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_block(block):
                print("Invalid Sudoku: Grid issue.")
                return

    print("Sudoku is valid.")

is_valid_sudoku()