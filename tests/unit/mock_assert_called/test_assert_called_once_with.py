import pytest
from unittest.mock import Mock
from src.reserva_produto import ReservaProduto


def test_o_motor_deve_ser_ligado():
    
    mock_reserva = Mock(spec=ReservaProduto)

    mock_reserva.gerar_reserva_produto.return_value = True
    mock_reserva.gerar_reserva_produto(1)

    mock_reserva.gerar_reserva_produto.assert_called_once_with(1)