from hw.mikita_karmanaw.donotmerge.task import decor
from hw.mikita_karmanaw.donotmerge.task import func


@decor
def test_01() -> None:
    assert func() > 1
