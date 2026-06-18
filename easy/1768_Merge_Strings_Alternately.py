def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    lent = len(word2) if len(word1) >= len(word2) else len(word1)
    for i in range(lent):
        result += word1[i]
        result += word2[i]
    if lent == len(word1):
        result += word2[i + 1::]
    else:
        result += word1[i + 1::]
    return result
