from math import sqrt
from typing import Union

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(sequence: Union[str, list, tuple]) -> tuple:
    return sequence[0], sequence[-1]


def task_02_expand(
    sequence: Union[str, list, tuple]
) -> Union[str, list, tuple]:
    return int(sequence[0]) * sequence[1:]


def task_03_hdist(
    seq1: Union[str, list, tuple], seq2: Union[str, list, tuple]
) -> int:
    dist = abs(len(seq1) - len(seq2))
    arch = zip(seq1, seq2)
    for elem in arch:
        if elem[0] != elem[1]:
            dist += 1
    return dist


def distance(city1: tuple, city2: tuple) -> float:
    dist_0 = (city1[0] - city2[0]) * 111
    dist_1 = (city1[1] - city2[1]) * 65
    return sqrt((dist_0**2) + (dist_1**2))


def task_04_cities(city: str) -> dict:
    dist_dict = {}
    for town in CITIES:
        dist = distance(CITIES[city], CITIES[town])
        dist_dict[town] = dist
    return dist_dict


def task_05_route(route: Union[tuple, list]) -> float:
    dist = float(0)
    for town in route[1:]:
        previous_town_cords = CITIES[route[route.index(town) - 1]]
        dist += distance(CITIES[town], previous_town_cords)
    return dist
