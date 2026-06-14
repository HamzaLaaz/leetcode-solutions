def mapWordWeights(words: list[str], weights: list[int]) -> str:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rev = alpha[::-1]
    result = ""
    for word in words:
        total = 0
        for char in word:
            total += weights[alpha.index(char)]
        result += rev[total % 26]
    return result
