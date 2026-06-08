def isValidSudoku(board: list[list[str]]) -> bool:
    correct = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for row in board:
        corct = list(correct)
        for n in row:
            if n == ".":
                continue
            if n in corct:
                corct.remove(n)
            else:
                return False
    for i in range(9):
        corct = list(correct)
        for j in range(9):
            if board[j][i] == ".":
                continue
            if board[j][i] in corct:
                corct.remove(board[j][i])
            else:
                return False
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            corct = list(correct)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in corct:
                        corct.remove(board[i][j])
                    else:
                        return False
    return True
