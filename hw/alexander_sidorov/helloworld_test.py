from .helloworld import helloworld


def test_helloworld() -> None:
    assert helloworld() == "Hello, world!"
