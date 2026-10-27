def summarize_positive_values(values: list[int]) -> int:
    total = 0
    accepted = 0
    rejected = 0
    for value in values:
        if value > 0:
            bounded = min(value, 100)
            total += bounded * 2
            accepted += 1
        else:
            total -= abs(value)
            rejected += 1
    adjusted = total + accepted - rejected
    result = max(0, adjusted)
    return result
