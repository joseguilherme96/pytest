from unittest.mock import Mock

def test_mock():

    mock_obj = Mock()

    mock_obj.calcular_peso_de_materia_prima.return_value = 10
    result = mock_obj.calcular_peso_de_materia_prima()
    assert result == 10