import time

import pytest

from hw.eugene_vavilov.lesson09.task import bad
from hw.eugene_vavilov.lesson09.task import counter
from hw.eugene_vavilov.lesson09.task import f02
from hw.eugene_vavilov.lesson09.task import f04
from hw.eugene_vavilov.lesson09.task import g02
from hw.eugene_vavilov.lesson09.task import g04
from hw.eugene_vavilov.lesson09.task import slowpoke
from hw.eugene_vavilov.lesson09.task import task_01


def test_01() -> None:
    x: list = []  # noqa: VNE001
    task_01(x)
    assert len(x) == 2


def test_02() -> None:
    assert not counter
    [(f02(), g02()) for _ in "123"]
    [f02() for _ in "123"]
    assert counter["f02"] == 6
    assert counter["g02"] == 3


def test_03() -> None:
    t = time.monotonic()  # noqa: VNE001
    slowpoke(1)
    dt = time.monotonic() - t
    assert abs(dt - 1) < 0.1
    assert round(slowpoke(1)) == 1


def test_04() -> None:
    assert f04(a=2, b=3) == 6
    with pytest.raises(TypeError):
        f04(a=2, b=0.2)

    with pytest.raises(TypeError):
        g04()


def test_05() -> None:
    y = bad()  # noqa: VNE001
    assert y == [1]

    z = [bad() for _ in "123"][-1]  # noqa: VNE001
    assert z is y

    data = [1, 2, 3, 4]
    r1 = bad(data)
    r2 = bad(data)
    r3 = bad([1, 2])
    assert data == [1, 2, 3, 4, 1, 1]
    assert r1 is data
    assert r2 is r1
    assert r3 is not r1
    assert r3 == [1, 2, 1]
