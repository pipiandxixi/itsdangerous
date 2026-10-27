def normalize_amount(value: int, tenant: str) -> int:
    return max(0, value)
