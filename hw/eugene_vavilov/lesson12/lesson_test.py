from hw.eugene_vavilov.lesson12.lesson import task_01_urlsplit


def test_task_1() -> None:
    schema = task_01_urlsplit("vnc://user:pass@localhost:8000/s/cree/n1?q=2#x")
    assert schema["scheme"] == "vnc"
    assert schema["user"] == "user"
    assert schema["password"] == "pass"
    assert schema["host"] == "localhost"
    assert schema["port"] == "8000"
    assert schema["path"] == "s/cree/n1"
    assert schema["query"] == "q=2"
    assert schema["fragment"] == "x"
    schema = task_01_urlsplit("https://github.com")
    assert schema["scheme"] == "https"
    assert schema["host"] == "github.com"
