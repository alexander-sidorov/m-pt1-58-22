from typing import Any
from math import sqrt
from typing import Sequence

# from hw.alexander_sidorov.helpers import CITIES


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


def dist(*city) -> float:
    new_city = [city]
    if len(city) == 2 and city[0][0] < city[1][0]:
        total_att = city[1][0] - city[0][0] * 111
        total_lng = city[1][1] - city[0][1] * 65
        return sqrt((total_att**2) + (total_lng**2))
    elif len(city) == 2 and city[0][0] > city[1][0]:
        total_att = city[0][0] - city[1][0] * 111
        total_lng = city[0][1] - city[1][1] * 65
        return sqrt((total_att**2) + (total_lng**2))


print(dist((52.534754, 24.984273), (53.132227, 26.017363), (12, 10)))
