from functools import partial
from itertools import pairwise
from math import sqrt
from typing import Sequence
from typing import TypeVar

from hw.alexander_sidorov.helpers import CITIES

T = TypeVar("T")


def task_01_boundary(seq: Sequence[T]) -> tuple[T, T]:
    return seq[0], seq[-1]


def task_02_expand(seq: Sequence[T]) -> Sequence[T]:
    return seq[0] * seq[1:]  # type: ignore


def task_03_hdist(seq1: Sequence, seq2: Sequence) -> int:
    diff: int = sum(e1 != e2 for e1, e2 in zip(seq1, seq2))

    return diff + abs(len(seq1) - len(seq2))


PointT = tuple[float, float]


def distance(p1: PointT, p2: PointT) -> float:
    alat, alon = [c1 - c2 for c1, c2 in zip(p1, p2)]
    dlat, dlon = [angle * arc for angle, arc in [[alat, 111], [alon, 65]]]

    return sqrt(dlat**2 + dlon**2)


def task_04_cities(center: str) -> dict[str, float]:
    dist = partial(distance, CITIES[center])

    return {city: dist(coords) for city, coords in CITIES.items()}


def task_05_route(route: Sequence[str]) -> float:
    nodes = filter(bool, (CITIES.get(city) for city in route))
    edges = pairwise(nodes)
    distances = (distance(p0, p1) for p0, p1 in edges)  # type: ignore
    total = sum(distances)

    return total
