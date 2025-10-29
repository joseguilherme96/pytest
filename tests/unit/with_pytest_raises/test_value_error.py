import pytest

def get_produto(chave):

    produto = {"name":"Macarrão"}

    return produto[chave]


def test_chave_dicionario():

    with pytest.raises(KeyError):

        get_produto("ff")