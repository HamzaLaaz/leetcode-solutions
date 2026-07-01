def isPowerOfFour(n: int) -> bool:
    if n < 0:
        return False
    for i in range(16):
        result = 4 ** i
        if result == n:
            return True
    return False
