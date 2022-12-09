from typing import Any
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(sequence: Sequence) -> tuple:

    return sequence[0], sequence[-1]


def task_02_expand(sequence: Sequence) -> Any:

    return sequence[1:] * sequence[0]


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:

    if len(seq1) >= len(seq2):
        res = len(seq1) - len(seq2)
        for i in range(len(seq2)):
            if seq1[i] != seq2[i]:
                res += 1
    else:
        res = len(seq2) - len(seq1)
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                res += 1
    return res


def get_distance(point1: tuple, point2: tuple) -> Any:

    distance_x = (point1[0] - point2[0]) * 111
    distance_y = (point1[1] - point2[1]) * 65
    distance = pow(distance_x**2 + distance_y**2, 0.5)
    return distance


def task_04_cities(city: str) -> dict:

    dict_distance = {}
    for place, point in CITIES.items():
        dict_distance.update({place: get_distance(CITIES[city], point)})
    return dict_distance


def task_05_route(route: Sequence) -> int:

    distance = 0
    for city1, city2 in zip(route, route[1:]):
        distance += get_distance(CITIES[city1], CITIES[city2])
    return distance
