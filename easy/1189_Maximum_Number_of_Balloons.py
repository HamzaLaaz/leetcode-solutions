def maxNumberOfBalloons(text: str) -> int:
    d = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
    for c in text:
        if c in d:
            d[c] += 1
    result = d["b"]
    if d["a"] < result:
        result = d["a"]
    if d["l"] // 2 < result:
        result = d["l"] // 2
    if d["o"] // 2 < result:
        result = d["o"] // 2
    if d["n"] < result:
        result = d["n"]
    return result
