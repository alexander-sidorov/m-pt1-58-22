from typing import Any
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(sequence: Sequence) -> tuple:

    return sequence[0], sequence[-1]


def task_02_expand(sequence: Sequence) -> Any:

    return sequence[1:] * sequence[0]


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:

    return sum(True for i in zip(seq1, seq2) if i[0] != i[1]) + abs(
        len(seq1) - len(seq2)
    )


def get_distance(point1: tuple, point2: tuple) -> Any:

    d_x, d_y = (point1[0] - point2[0]) * 111, (point1[1] - point2[1]) * 65
    return (d_x ** 2 + d_y ** 2) ** 0.5


def task_04_cities(city: str) -> dict:

    return {k: get_distance(CITIES[city], v) for k, v in CITIES.items()}


def task_05_route(route: list | tuple) -> float:

    route_len, route_city = 0.0, [city for city in route if city in CITIES]
    for i in range(len(route_city) - 1):
        route_len += get_distance(
            CITIES[route_city[i]], CITIES[route_city[i + 1]]
        )
    return route_len
