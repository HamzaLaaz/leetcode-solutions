import copy


def rotate(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    new = copy.deepcopy(matrix)
    new = new[-1::-1]
    for n in range(len(new)):
        for i in range(len(new)):
            matrix[n][i] = new[i][n]
