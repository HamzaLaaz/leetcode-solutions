def itoa(num):
    result = ""
    while num > 0:
        result += chr(num % 10 + 48)
        num //= 10
    return result[::-1]

def addToArrayForm(num: list[int], k: int) -> list[int]:
    result = num[0]
    for n in num[1:]:
        result *= 10
        result += n
    ans = result + k
    new = []
    anss = itoa(ans)
    for i in anss:
        new.append(int(i))
    return new
