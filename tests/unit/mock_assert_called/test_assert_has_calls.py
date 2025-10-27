import pytest
from unittest.mock import Mock, call
from src.entrada_produto import EntradaProduto
from src.requisicao_produto import RequisicaoProduto
from src.reserva_produto import ReservaProduto
from src.baixa_produto import BaixaProduto

def test_baixa_produto():


    mock_baixa = Mock(spec=BaixaProduto)

    mock_baixa.entrada = Mock(spec=EntradaProduto)
    mock_baixa.requisicao = Mock(spec=RequisicaoProduto)
    mock_baixa.reserva = Mock(spec=ReservaProduto)

    mock_baixa.entrada.inserir_produto_no_estoque()
    mock_baixa.requisicao.criar_requisicao_produto()
    mock_baixa.reserva.gerar_reserva_produto(1)
    mock_baixa.baixar_produto_no_estoque()

    chamadas_esperadas = [
        call.entrada.inserir_produto_no_estoque(),
        call.requisicao.criar_requisicao_produto(),
        call.reserva.gerar_reserva_produto(1),
        call.baixar_produto_no_estoque()
    ]

    mock_baixa.assert_has_calls(chamadas_esperadas)

    

    