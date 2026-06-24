def calPoints(operations: list[str]) -> int:
    record = []
    for o in operations:
        if o == "D":
            record.append(record[-1] * 2)
        elif o == "C":
            record.pop()
        elif o == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(o))
    return sum(record)
