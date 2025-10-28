from src.cripto import get_chainlink_price


class MockResponse:
    @staticmethod
    def json():
        return{"value":100.43}
    


def test_get_chainlink_price(monkeypatch):

    monkeypatch.setattr("requests.get",lambda x: MockResponse())
    assert get_chainlink_price() == {"value":100.43}