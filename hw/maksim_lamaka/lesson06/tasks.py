from typing import Any
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(seq: Sequence) -> tuple:

    return seq[0], seq[-1]


def task_02_expand(seq1: Sequence) -> Any:

    return seq1[0] * seq1[1:]


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:
    dist = abs(len(seq1) - len(seq2))
    dist_zip = zip(seq1, seq2)
    for i in dist_zip:
        if i[0] != i[1]:
            dist += 1
    return dist


def task_04_cities(city: str) -> dict:
    total = {}
    for key in CITIES.keys():
        one = CITIES[city]
        two = CITIES[key]
        x, y = (one[0] - two[0]) * 111, (one[1] - two[1]) * 65
        distance = int((x**2 + y**2) ** 0.5)
        total.update({key: distance})
    return total


def task_05_route(route: Sequence) -> int:
    total = 0
    value: Any = ()
    for i in route:
        value = value + CITIES[i]
    first = value[0::2]  # type: tuple
    sec = value[1::2]  # type: tuple
    for ind in range(len(first) - 1):
        lon, lat = (first[ind] - first[ind + 1]) * 111, (
            sec[ind] - sec[ind + 1]
        ) * 65
        distance = int((lon**2 + lat**2) ** 0.5)
        total += distance
    return total
