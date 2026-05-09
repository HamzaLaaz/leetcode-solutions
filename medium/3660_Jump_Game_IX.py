def maxValue(nums: list[int]) -> list[int]:
    n = len(nums)
    suffix_min = [0] * n
    suffix_min[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(nums[i], suffix_min[i + 1])
    ans = [0] * n
    start = 0
    prefix_max = nums[0]
    for i in range(n - 1):
        prefix_max = max(prefix_max, nums[i])
        if prefix_max <= suffix_min[i + 1]:
            component_max = max(nums[start:i + 1])
            for j in range(start, i + 1):
                ans[j] = component_max
            start = i + 1
    component_max = max(nums[start:])
    for j in range(start, n):
        ans[j] = component_max
    return ans
