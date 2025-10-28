from pathlib import Path

def get_xls_path():

    return Path.home() / "documentos"

def test_get_xls_path(monkeypatch): 

    def mockreturn():

        return Path("/tmp")

    monkeypatch.setattr(Path, "home", mockreturn)

    assert get_xls_path() == Path("/tmp/documentos")