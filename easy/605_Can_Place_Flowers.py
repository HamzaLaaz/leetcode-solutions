def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    if len(flowerbed) == 1 and not flowerbed[0] and n > 0:
        n -= 1
        return n == 0
    if not flowerbed[0] and not flowerbed[1] and len(flowerbed) > 1 and n > 0:
        n -= 1
        flowerbed[0] += 1
    if (not flowerbed[-1] and not flowerbed[-2] and
            len(flowerbed) > 1 and n > 0):
        n -= 1
        flowerbed[-1] += 1
    for i in range(1, len(flowerbed) - 1):
        if (not flowerbed[i - 1] and not flowerbed[i] and
                not flowerbed[i + 1] and n > 0):
            n -= 1
            flowerbed[i] += 1
    return n == 0
