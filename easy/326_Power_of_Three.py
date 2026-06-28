def isPowerOfThree(n: int) -> bool:
    if n < 0:
        return False
    for i in range(31):
        result = 3 ** i
        if result == n:
            return True
    return False
