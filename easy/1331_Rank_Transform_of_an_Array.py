def arrayRankTransform(arr: list[int]) -> list[int]:
    d = {}
    for i, r in enumerate(sorted(set(arr)), 1):
        d[r] = i
    s = [d[r] for r in arr]
    return s
