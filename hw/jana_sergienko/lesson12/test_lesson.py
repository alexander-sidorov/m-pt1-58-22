from hw.jana_sergienko.lesson12.lesson import task_01_urlsplit


def test_task_01_urlsplit() -> None:
    comps = task_01_urlsplit('http://user:password@host:1234/resourse')
    assert comps("scheme") == "http"
    assert comps("userinfo") == "user:password"
    assert comps("host") == "host"
    assert comps("port") == "1234"
