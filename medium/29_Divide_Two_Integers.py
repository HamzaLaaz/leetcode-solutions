def divide(dividend: int, divisor: int) -> int:
    k = 0
    if divisor < 0:
        k += 1
        divisor *= -1
    if dividend < 0:
        k += 1
        dividend *= -1
    total = dividend // divisor
    if k > 1 or not k:
        if total > 2147483647:
            return 2147483647
        return total
    else:
        if total < -2147483648:
            return -2147483648
        return -total
