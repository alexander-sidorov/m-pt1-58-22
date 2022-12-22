import math
from typing import Any
from typing import Sequence

from hw.alexander_sidorov.helpers import CITIES


def task_01_boundary(_seq1: Sequence) -> tuple:
    _element_1 = _seq1[0]
    _element_2 = _seq1[-1]
    return _element_1, _element_2


def task_02_expand(_seq1: Sequence) -> Any:
    return _seq1[1:] * _seq1[0]


def task_03_hdist(_seq1: Sequence, _seq2: Sequence) -> int:
    distance = 0
    if len(_seq1) > len(_seq2):
        _seq1, _seq2 = _seq2, _seq1
    for i in range(len(_seq1)):
        if str(_seq1[i]) != str(_seq2[i]):
            distance += 1
    distance += len(_seq2) - len(_seq1)
    return distance


def _cities_distance(_user_town: str, _town: str) -> int:
    _par = CITIES[_user_town][0] - CITIES[_town][0]
    _shir = CITIES[_user_town][1] - CITIES[_town][1]
    _par *= 111
    _shir *= 65
    _distance = math.sqrt((_par**2) + (_shir**2))
    _distance = round(_distance)
    return _distance


def task_04_cities(_user_town: str) -> dict:
    _maps = {}
    for _i in CITIES:
        _maps.update({_i: _cities_distance(_user_town, _i)})
    return _maps


def task_05_route(_route: Sequence) -> int:
    _total_distance = 0
    _last_town = _route[0]
    for _i in _route:
        if _i not in CITIES:
            _i = _last_town
        _total_distance += _cities_distance(_last_town, _i)
        _last_town = _i
    return _total_distance
