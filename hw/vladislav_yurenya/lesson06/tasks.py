from math import floor
from typing import Any
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(sequence: Sequence) -> tuple:
    return tuple(sequence[0] + sequence[-1])


def task_02_expand(sequence: Sequence) -> Any:
    seq = sequence[0]
    del sequence[0]
    return sequence * seq


def f(seq1, seq2):
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
    for x in zip(seq1, seq2):
        if x[0] != x[1]:
            total += 1
    return total


def calculation(first, second):
    x, y = (first[0] - second[0]) * 111, (first[1] - second[1]) * 65
    return floor((x**2 + y**2) ** 0.5)


def task_04_cities(city: str) -> dict:
    total = {}
    for key in CITIES.keys():
        first = CITIES.get(city)
        second = CITIES.get(key)
        calculation(first, second)
        new_dict = dict([(key, calculation(first, second))])
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
