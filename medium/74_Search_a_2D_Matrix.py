def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for i in range(len(matrix)):
        for nb in matrix[i]:
            if nb == target:
                return True
    return False
