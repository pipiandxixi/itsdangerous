from codegov_acceptance.domain.api import normalize_amount


def quote(value: int) -> int:
    return normalize_amount(value)
