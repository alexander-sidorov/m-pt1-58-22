from typing import Any
from math import sqrt
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(suquence: Sequence) -> tuple:
    return suquence[0], suquence[-1]


def task_02_expand(suquence: Sequence) -> None:
    return suquence[1:] * suquence[0]


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:
    y = 0
    res = [x for x in seq1 + seq2 if x not in seq1 or x not in seq2]
    if len(res) > 0:
        y = y + len(res)
        return y
    else:
        return y


def dist(city1: tuple, city2: tuple) -> float:
    total_att = city1[0] - city2[0] * 111
    total_lng = city1[1] - city2[1] * 65
    return sqrt((total_att**2) + (total_lng**2))


def task_04_cities(city: str) -> dict:
    dist_dict = {}
    for town in CITIES:
        dist = dist(CITIES[city], CITIES[town])
        dist_dict[town] = dist
    return dist_dict


print(task_04_cities("Минск"))
