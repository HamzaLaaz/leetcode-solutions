def generate(self, numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[1]]
    Rows = [[1], [1, 1]]
    for i in range(1, numRows - 1):
        new = [1]
        for j in range(i):
            new.append(Rows[i][j] + Rows[i][j + 1])
        new.append(1)
        Rows.append(new)
    return Rows
