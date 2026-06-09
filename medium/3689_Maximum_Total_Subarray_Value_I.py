def maxTotalValue(nums: list[int], k: int) -> int:
    return k * (max(nums) - min(nums))
