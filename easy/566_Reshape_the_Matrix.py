def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    new = []
    for m in mat:
        for i in m:
            new.append(i)
    result = []
    if r == 1:
        result.append(new)
        return result
    k = 0
    if len(new) != r * c:
        return mat
    while r >= 1:
        row = []
        for _ in range(c):
            if k < len(new):
                row.append(new[k])
                k += 1
        r -= 1
        result.append(row)
    return result
