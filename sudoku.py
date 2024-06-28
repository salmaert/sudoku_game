def is_valid_sudoku(board):
    def is_valid_group(group):
        return set(group) == set('123456789')

    def get_subsquare(board, row, col):
        return [board[r][c] for r in range(row, row+3) for c in range(col, col+3)]

    # Check rows
    for row in board:
        if not is_valid_group(row):
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False

    # Check 3x3 sub-squares
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subsquare = get_subsquare(board, row, col)
            if not is_valid_group(subsquare):
                return False

    return True

def main():
    board = []
    print("Enter the Sudoku board (9 lines of 9 digits):")
    for _ in range(9):
        line = input()
        if len(line) != 9 or not line.isdigit():
            print("Invalid input. Each line must contain exactly 9 digits.")
            return
        board.append(line)

    if is_valid_sudoku(board):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
