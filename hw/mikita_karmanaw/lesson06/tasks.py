from math import sqrt
from typing import Union

CITIES = {
    "Барановичи": (53.132227, 26.017363),
    "Берёза": (52.534754, 24.984273),
    "Бобруйск": (53.145646, 29.225297),
    "Борисов": (54.224141, 28.511507),
    "Браслав": (55.639499, 27.031569),
    "Брест": (52.093721, 23.684757),
    "Витебск": (55.184204, 30.202767),
    "Волковыск": (53.162982, 24.463780),
    "Глубокое": (55.138798, 27.685619),
    "Гомель": (52.424280, 31.014063),
    "Гродно": (53.677764, 23.829300),
    "Житковичи": (52.217048, 27.854883),
    "Жлобин": (52.892235, 30.037624),
    "Жодино": (54.094370, 28.321572),
    "Кобрин": (52.208612, 24.354257),
    "Лепель": (54.886647, 28.693817),
    "Лида": (53.891662, 25.302200),
    "Минск": (53.902735, 27.555696),
    "Мозырь": (52.049078, 29.267184),
    "Молодечно": (54.307345, 26.838960),
    "Орша": (54.510823, 30.429367),
    "Пинск": (52.111481, 26.102166),
    "Полоцк": (55.485590, 28.767977),
    "Поставы": (55.113615, 26.839303),
    "Речица": (52.371565, 30.386450),
    "Светлогорск": (52.633044, 29.748194),
    "Слуцк": (53.027615, 27.552063),
    "Солигорск": (52.792866, 27.543479),
}


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
        dist = sqrt(
            ((CITIES[city][0] - CITIES[town][0]) * 110) ** 2
            + ((CITIES[city][1] - CITIES[town][1]) * 65) ** 2
        )
        dist_dict.update({town: dist})
    return dist_dict


def task_05_route(route: Union[tuple, list]) -> float:
    dist = float(0)
    for town in route[1:]:
        dist += sqrt(
            ((CITIES[town][0] - CITIES[route[route.index(town) - 1]][0]) * 110)
            ** 2
            + (
                (CITIES[town][1] - CITIES[route[route.index(town) - 1]][1])
                * 65
            )
            ** 2
        )
    return dist
