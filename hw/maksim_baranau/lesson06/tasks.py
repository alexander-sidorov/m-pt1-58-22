from typing import Union
from math import sqrt
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
    distant = abs(len(seq1) - len(seq2))
    mdistant = min(len(seq1), len(seq2))
    for i in range(mdistant):
        if seq1[i] != seq2[i]:
            distant += 1
    return distant


def distance(point1: tuple, point2: tuple) -> float:
    distance_x = (point1[0] - point2[0]) * 111
    distance_y = (point1[1] - point2[1]) * 65
    pif = sqrt((distance_x) ** 2 + (distance_y**2))
    return pif


def task_04_cities(city: str) -> dict:
    distance_dict = {}
    for gorod in CITIES:
        dist = distance(CITIES[city], CITIES[gorod])
        distance_dict[gorod] = dist
    return distance_dict


def task_05_route(route: Union[tuple, list]) -> float:
    dist = float(0)
    for i in route[1:]:
        gorod_next = CITIES[route[route.index(i) - 1]]
        gorod_len = distance(CITIES[i], gorod_next)
        dist = dist + gorod_len
    return int(dist)
