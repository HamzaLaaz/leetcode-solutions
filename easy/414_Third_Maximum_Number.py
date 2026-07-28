def thirdMax(nums: list[int]) -> int:
    n = list(set(nums))
    if len(n) <= 2:
        return max(n)
    for _ in  range(2):
        k = max(n)
        n.pop(n.index(k))
    return max(n)
