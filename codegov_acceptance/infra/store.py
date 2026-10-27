from codegov_acceptance.domain.api import normalize_amount


def load(value: int) -> int:
    return normalize_amount(value)
