from typing import Sequence
from typing import Any
from math import sqrt

from hw.alexander_sidorov.helpers import CITIES

def task_01_boundary(sequence: Sequence) -> tuple:
    return tuple(sequence[0] + sequence[-1])


def task_02_expand(sequence: Sequence) -> Any:
    return sequence[1:] * int(sequence[0])


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:
    val = abs(len(seq1) - len(seq2))
    zip_val = zip(seq1, seq2)
    for i in zip_val:
        if zip_val[0] != zip_val[1]:
            val += 1
        return val


def task_04_cities(city: str) -> dict:
    val = {}
    for i in CITIES.keys():
        val_1 = CITIES[city]
        val_2 = CITIES[i]
        x, y = (val_1[0] - val_2[0]) * 111, (val_1[1] - val_2[1]) * 65
        distance = int((x ** 2 + y ** 2) ** 0.5)
        val.update({i: distance})
    return val


def task_05_route(route: Sequence) -> float:
    def distance(city1: tuple, city2: tuple) -> float:
        value_0 = (city1[0] - city2[0]) * 111
        value_1 = (city1[1] - city2[1]) * 65
        return sqrt((value_0 ** 2) + (value_1 ** 2))
    dist = float(0)
    for town in route[1:]:
        previous_town_cords = CITIES[route[route.index(town) - 1]]
        dist += distance(CITIES[town], previous_town_cords)
    return dist
