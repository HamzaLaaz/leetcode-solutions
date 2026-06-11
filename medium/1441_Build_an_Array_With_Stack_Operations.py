def buildArray(target: list[int], n: int) -> list[str]:
    new = []
    for i in range(1, target[-1] + 1):
        new.append("Push")
        if i in target:
            continue
        else:
            new.append("Pop")
    return new
