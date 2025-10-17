from src.produto import Produto
from unittest.mock import create_autospec


def test_autorizar_produto():

    mock_autorizar = create_autospec(Produto)
    mock_autorizar.autorizar_produto.return_value = True

    result = mock_autorizar.autorizar_produto(1)

    assert result == True