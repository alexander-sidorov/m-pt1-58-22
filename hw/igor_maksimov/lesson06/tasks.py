from typing import Sequence
from typing import Any
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


def task_04_cities(city: str) -> float:
    print(CITIES)


task_04_cities()
