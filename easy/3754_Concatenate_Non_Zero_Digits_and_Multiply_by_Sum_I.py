def sumAndMultiply(n: int) -> int:
    s = str(n)
    new = [i for i in s if i != "0"]
    Sum = 0
    x = 0
    for k in new:
        num = int(k)
        Sum += num
        x = (x * 10) + num
    return x * Sum
