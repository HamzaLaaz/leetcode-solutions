import math


def gcdOfOddEvenSums(n: int) -> int:
    sumodd = 0
    sumeven = 0

    for i in range(1, n + 1):
        if i % 2:
            sumodd += i
        else:
            sumeven += i
    return math.gcd(sumodd, sumeven) if math.gcd(sumodd, sumeven) >= n else n
