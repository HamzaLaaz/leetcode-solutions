def addDigits(num: int) -> int:
    num_s = str(num)
    result = 0
    for i in range(len(num_s)):
        result += int(num_s[i])
    while result > 9:
        num_s = str(result)
        result = 0
        for i in range(len(num_s)):
            result += int(num_s[i])
    return result
