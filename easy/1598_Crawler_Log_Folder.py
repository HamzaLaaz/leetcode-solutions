def minOperations(logs: list[str]) -> int:
    result = 0
    for log in logs:
        if log == "./":
            continue
        elif log == "../" and result > 0:
            result -= 1
        elif log[-1] == "/" and log[0] != ".":
            result += 1
        else:
            continue
    return result
