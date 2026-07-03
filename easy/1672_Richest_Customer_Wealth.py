def maximumWealth(accounts: list[list[int]]) -> int:
    new = []
    for nums in accounts:
        result = 0
        for n in nums:
            result += n
            new.append(result)
    return max(new)
