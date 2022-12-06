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
    if len(seq1) >= len(seq2):
        larger = seq1
        lesser = seq2
    else:
        larger = seq2
        lesser = seq1
    for elem in lesser:
        if elem != larger[lesser.index(elem)]:
            dist += 1
    return dist


def task_04_cities(city: str) -> dict:
    dist_dict = {}
    for town in CITIES:
        dist_0 = (CITIES[city][0] - CITIES[town][0]) * 111
        dist_1 = (CITIES[city][1] - CITIES[town][1]) * 65
        dist = sqrt((dist_0**2) + (dist_1**2))
        dist_dict.update({town: dist})
    return dist_dict


def task_05_route(route: Union[tuple, list]) -> float:
    dist = float(0)
    for town in route[1:]:
        dist_0 = (
            CITIES[town][0] - CITIES[route[route.index(town) - 1]][0]
        ) * 111
        dist_1 = (
            CITIES[town][1] - CITIES[route[route.index(town) - 1]][1]
        ) * 65
        dist += sqrt(dist_0**2 + dist_1**2)
    return dist
