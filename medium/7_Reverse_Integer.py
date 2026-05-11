def reverse(x: int) -> int:
    if x >= 0:
        s = str(x)
        return int(s[-1::-1]) if int(s[-1::-1]) <= 2147483647 else 0
    else:
        x *= -1
        s = str(x)
        return -1 * int(s[-1::-1]) if (-1 * int(s[-1::-1])) >= -2147483648 else 0

