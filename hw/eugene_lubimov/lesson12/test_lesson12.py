import hw.eugene_lubimov.lesson12.lesson12 as les


def test_pars_url() -> None:

    url = "https://digitology.tech/docs/python_3/library/urllib.parse.html"

    my_d = les.pars_url(url)

    assert my_d["scheme"] == "https"


def test_request() -> None:

    req = """HEAD /docs/python_3/library/urllib.parse.html HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: digitology.tech
User-Agent: HTTPie/3.2.1


"""
    req1 = les.Request(req)

    assert req1.method() == "HEAD"
    assert req1.path() == "/docs/python_3/library/urllib.parse.html"
    assert req1.version() == "HTTP/1.1"
    assert req1.headers()["Accept"] == "*/*"
    assert req1.body() == ""
