def check(nums: list[int]) -> bool:
    is_sorted = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
    if is_sorted:
        return is_sorted
    else:
        k = len(nums)
        while k > 0:
            tmp = nums.pop()
            nums.insert(0, tmp)
            is_sorted = all(nums[i] <= nums[i + 1]
                            for i in range(len(nums) - 1))
            if is_sorted:
                return is_sorted
            k -= 1
        return False
