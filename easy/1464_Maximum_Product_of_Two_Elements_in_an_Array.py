def maxProduct(nums: list[int]) -> int:
    n1 = max(nums)
    nums.pop(nums.index(n1))
    n2 = max(nums)
    return (n1 - 1) * (n2 - 1)
