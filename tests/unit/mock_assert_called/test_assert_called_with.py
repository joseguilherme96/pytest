import pytest
from unittest.mock import Mock
from src.localizacao_drone import LocalizacaoDrone


def test_enviar_localizacao():

    mock_localizacao = Mock(LocalizacaoDrone)

    mock_localizacao.get_localizacao.return_value = [32222,33322]
    latitude,longitude = mock_localizacao.get_localizacao()

    mock_localizacao.enviar_localizacao.return_value = 201
    assert mock_localizacao.enviar_localizacao(latitude,longitude) == 201

    mock_localizacao.enviar_localizacao.assert_called_with(latitude,longitude)