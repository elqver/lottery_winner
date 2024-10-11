PLUS_BASE_VALUE = 1
MINUS_BASE_SCORE = -10
EQUAL_BASE_SCORE = -100


def index_to_multiplier(index: int) -> int:
    return index + 1


def plus_score(index: int) -> int:
    return PLUS_BASE_VALUE * index_to_multiplier(index)


def minus_score(index: int) -> int:
    return MINUS_BASE_SCORE * index_to_multiplier(index)


def equals_score(index: int) -> int:
    return EQUAL_BASE_SCORE * index_to_multiplier(index)


def score(line: list[str]) -> int:
    res = 0
    for index, value in enumerate(line):
        if value == '+':
            res += plus_score(index)
        elif value == '-':
            res += minus_score(index)
        elif value == '=':
            res += equals_score(index)

    return res
