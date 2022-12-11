from math import floor
from typing import Any
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(sequence: Sequence) -> tuple:
    return tuple(sequence[0] + sequence[-1])


def task_02_expand(sequence: Sequence) -> Any:
    return sequence[1:] * sequence[0]


def f(seq1: Sequence, seq2: Sequence) -> str:
    if len(seq1) < len(seq2):
        seq1 += " " * (len(seq2) - len(seq1))
        return seq1
    else:
        seq2 += " " * (len(seq1) - len(seq2))
        return seq2


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:
    total = 0
    seq1 = list(seq1)
    seq2 = list(seq2)
    f(seq1, seq2)
    for zip_seq in zip(seq1, seq2):
        if zip_seq[0] != zip_seq[1]:
            total += 1
    return total


def calculation(one: tuple, two: tuple) -> Any:
    x, y = (one[0] - two[0]) * 111, (one[1] - two[1]) * 65
    return floor((x**2 + y**2) ** 0.5)


def task_04_cities(city: str) -> dict:
    total = {}
    for key in CITIES.keys():
        one = CITIES.get(city)
        two = CITIES.get(key)
        calculation(one, two)
        new_dict = dict([(key, calculation(one, two))])
        total.update(new_dict)
    return total


def task_05_route(route: Sequence) -> int:
    total = 0
    for first, second in zip(route, route[1:]):
        one = CITIES.get(first)
        two = CITIES.get(second)
        calculation(one, two)
        total += calculation(one, two)
    return total