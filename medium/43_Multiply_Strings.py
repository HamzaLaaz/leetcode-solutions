def atoi(nb):
    sign = 1
    i = 0
    n = 0
    if nb[0] == '-':
        sign = -1
        i = 1
    while i < len(nb):
        n += ord(nb[i]) - 48
        n *= 10
        i += 1
    n //= 10
    return n * sign


def itoa(nb):
    n = ""
    if nb < 0:
        n += '-'
        nb *= -1
    while nb > 0:
        t = nb % 10
        n += chr(t + 48)
        nb //= 10
    if n:
        return n[::-1]
    return "0"


def multiply(num1: str, num2: str) -> str:
    total = atoi(num1) * atoi(num2)
    return itoa(total)
