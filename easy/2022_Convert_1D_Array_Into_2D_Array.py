def construct2DArray(original: list[int], m: int, n: int) -> list[list[int]]:
    if n * m < len(original):
        return []
    i = 0
    result = []
    for _ in range(m):
        row = []
        for _ in range(n):
            if i < len(original):
                row.append(original[i])
                i += 1
            else:
                return []
        result.append(row)
    return result
