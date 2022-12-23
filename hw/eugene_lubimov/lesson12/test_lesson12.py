import hw.eugene_lubimov.lesson12.lesson12 as les


def test_pars_url() -> None:

    url = "https://digitology.tech/docs/python_3/library/urllib.parse.html"

    my_d = les.pars_url(url)

    assert my_d["scheme"] == "https"
