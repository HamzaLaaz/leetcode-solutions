def maxProfit(prices: list[int]) -> int:
    result = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            result = max(result, prices[i] - min_price)
    return result
