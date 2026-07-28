def atoi(num):
    result = 0
    for nb in num:
        result += int(nb)
        result *= 10
    result //= 10
    return result

def itoa(num):
    result = ""
    while num > 0:
        result += chr((num % 10) + 48)
        num //= 10
    return result[::-1]

def addStrings(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return num1 if num2 == "0" else num2
    n1 = atoi(num1)
    n2 = atoi(num2)
    result = n1 + n2
    return itoa(result)
