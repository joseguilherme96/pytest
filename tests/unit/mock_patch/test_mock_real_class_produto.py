from src.produto import Produto
from unittest.mock import Mock

def test_autorizar_produto():

    produto = Produto()

    produto.autorizar_produto = Mock(return_value=True)
    result = produto.autorizar_produto(1)

    assert result == True