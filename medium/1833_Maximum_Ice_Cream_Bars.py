def maxIceCream(costs: list[int], coins: int) -> int:
    costs.sort()
    count = 0
    for cost in costs:
        if cost <= coins:
            count += 1
            coins -= cost
        else:
            return count
    return count
