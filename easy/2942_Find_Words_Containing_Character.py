def findWordsContaining(words: list[str], x: str) -> list[int]:
    new = []
    for i, word in enumerate(words):
        if x in word:
            new.append(i)
    return new
