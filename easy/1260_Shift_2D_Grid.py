def shiftGrid(grid: list[list[int]], k: int) -> list[list[int]]:
    lt = len(grid[0])
    new = []
    for r in grid:
        for n in r:
            new.append(n)
    while k > 0:
        new.insert(0, new[-1])
        new.pop()
        k -= 1
    result = []
    for i in range(0, len(new), lt):
        result.append(new[i:i + lt])
    return result
