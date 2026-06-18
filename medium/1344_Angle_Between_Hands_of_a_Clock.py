def angleClock(hour: int, minutes: int) -> float:
    minute_angle = minutes * 6
    hour_angle = hour * 30 + minutes * 0.5
    result = abs(hour_angle - minute_angle)
    return result if result < 180 else 360 - result
