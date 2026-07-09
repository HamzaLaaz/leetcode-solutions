def pathExistenceQueries(
    n: int,
    nums: list[int],
    maxDiff: int,
    queries: list[list[int]]
        ) -> list[bool]:
    component = [0] * n
    comp = 0
    for i in range(1, n):
        if nums[i] - nums[i - 1] > maxDiff:
            comp += 1
        component[i] = comp
    new = []
    for lf, r in queries:
        new.append(component[lf] == component[r])
    return new
