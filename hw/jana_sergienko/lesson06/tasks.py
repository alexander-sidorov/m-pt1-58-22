from math import sqrt
from typing import Sequence
from typing import Any

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(sequence: Sequence) -> tuple:
    return tuple(sequence[0] + sequence[-1])


def task_02_expand(sequence: Sequence) -> Any:
    return sequence[1:] * sequence[0]


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:
    alt = 0
    alt = abs(len(seq1) - len(seq2))
    zip_alt = zip(seq1, seq2)
    for i in zip_alt:
        if i[0] != i[1]:
            alt += 1
    return alt


def task_04_cities(city: str) -> dict:
    alt = {}
    for i in CITIES.keys():
        alt_1 = CITIES[city]
        alt_2 = CITIES[i]
        x, y = (alt_1[0] - alt_2[0]) * 111, (alt_1[1] - alt_2[1]) * 65
        distance = int((x ** 2 + y ** 2) ** 0.5)
        alt.update({i: distance})
    return alt


def distance(city1: tuple, city2: tuple) -> float:
    value_0 = (city1[0] - city2[0]) * 111
    value_1 = (city1[1] - city2[1]) * 65
    return sqrt((value_0 ** 2) + (value_1 ** 2))


def task_05_route(route: Sequence) -> float:
    dist = float(0)
    for town in route[1:]:
        previous_town_cords = CITIES[route[route.index(town) - 1]]
        dist += distance(CITIES[town], previous_town_cords)
    return dist
