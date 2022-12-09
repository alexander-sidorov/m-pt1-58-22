import typing

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(sequence: typing.Sequence) -> tuple:
    tup = (sequence[0], sequence[-1])
    return tup


def task_02_expand(sequence: typing.Sequence) -> typing.Sequence:
    return sequence[1:] * int(sequence[0])


def task_03_hdist(seq1: typing.Sequence, seq2: typing.Sequence) -> int:
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


def task_04_cities(city: str) -> dict:
    dict_distance = {}
    for place in CITIES:
        x = (CITIES[city][0] - CITIES[place][0]) * 111
        y = (CITIES[city][1] - CITIES[place][1]) * 65
        distance = pow(x ** 2 + y ** 2, 0.5)
        dict_distance.update({place: distance})
    return dict_distance


def task_05_route(route: typing.Sequence) -> int:
    distance = 0
    for city1, city2 in zip(route, route[1:]):
        x = (CITIES[city1][0] - CITIES[city2][0]) * 111
        y = (CITIES[city1][1] - CITIES[city2][1]) * 65
        distance += pow(x ** 2 + y ** 2, 0.5)
    return distance
