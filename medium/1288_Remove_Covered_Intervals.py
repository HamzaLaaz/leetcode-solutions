def removeCoveredIntervals(intervals: list[list[int]]) -> int:
    covered = len(intervals)
    for i in range(len(intervals)):
        for j in range(len(intervals)):
            if i == j:
                continue
            if (intervals[j][0] <= intervals[i][0] and
                    intervals[i][1] <= intervals[j][1]):
                covered -= 1
                break
    return covered
