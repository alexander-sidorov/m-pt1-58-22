from math import sqrt
from typing import Any
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(seq: Sequence) -> tuple:

    return seq[0], seq[-1]


def task_02_expand(seq: Sequence) -> Any:

    return seq[0] * seq[1:]


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:
    dist = abs(len(seq2) - len(seq1))
    zipped = zip(seq1, seq2)
    for first_pair in zipped:
        if first_pair[0] != first_pair[1]:
            dist += 1
    return dist


def calc_dist(x_coord: float, y_coord: float, mul: int) -> float:

    return (x_coord - y_coord) * mul


def get_dist(city1: tuple, city2: tuple) -> float:
    dist_0 = calc_dist(city1[0], city2[0], 111)
    dist_1 = calc_dist(city1[1], city2[1], 65)
    return sqrt((dist_0**2) + (dist_1**2))


def task_04_cities(start_city: str) -> dict:
    res_dist = {}
    for dest_city in CITIES:
        dist = get_dist(CITIES[start_city], CITIES[dest_city])
        res_dist[dest_city] = dist
    return res_dist


def task_05_route(route: list | tuple) -> float:
    dist = 0.0
    real_cities = [city for city in route if city in CITIES]
    for count in range(len(real_cities) - 1):
        dist += get_dist(
            CITIES[real_cities[count]], CITIES[real_cities[count + 1]]
        )
    return dist
