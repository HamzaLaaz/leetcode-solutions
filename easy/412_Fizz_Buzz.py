def fizzBuzz(n: int) -> list[str]:
    new = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            new.append("FizzBuzz")
        elif i % 5 == 0:
            new.append("Buzz")
        elif i % 3 == 0:
            new.append("Fizz")
        else:
            s = str(i)
            new.append(s)
    return new
