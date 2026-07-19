def removeKdigits(num: str, k: int) -> str:
    nums = []
    for n in num:
        while nums and nums[-1] > n and k > 0:
            nums.pop()
            k -= 1
        nums.append(n)
    while k > 0:
        nums.pop()
        k -= 1
    while nums and nums[0] == "0":
        nums.pop(0)
    result = "".join(nums)
    return result if result else "0"
