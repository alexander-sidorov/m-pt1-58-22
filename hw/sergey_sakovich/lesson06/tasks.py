from typing import Any
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(sequence: Sequence) -> tuple:

    return sequence[0], sequence[-1]


def task_02_expand(sequence: Sequence) -> Any:

    return sequence[1:] * sequence[0]


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:

    if len(seq1) >= len(seq2):
        seq = len(seq1) - len(seq2)
        for i in range(len(seq2)):
            if seq1[i] != seq2[i]:
                seq += 1
    else:
        seq = len(seq2) - len(seq1)
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                seq += 1
    return seq


def length(point1: tuple, point2: tuple) -> Any:

    distance = (
        ((point1[0] - point2[0]) * 110) ** 2
        + ((point1[1] - point2[1]) * 65) ** 2
    ) ** 0.5
    return distance


def task_04_cities(city: str) -> dict:

    dictionary = {}
    point1 = CITIES[city]
    for town in CITIES:
        point2 = CITIES[town]
        dictionary.update({town: length(point1, point2)})
    return dictionary


def task_05_route(route: Sequence) -> float:

    distance = 0
    for city1, city2 in zip(route, route[1:]):
        distance += length(CITIES[city1], CITIES[city2])
    return distance
