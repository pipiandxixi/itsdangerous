from codegov_acceptance.infra.store import load


def normalize_amount(value: int) -> int:
    return max(0, value)


def load_amount(value: int) -> int:
    return load(value)
