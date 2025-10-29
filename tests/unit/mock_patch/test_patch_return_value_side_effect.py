from unittest.mock import patch
import pytest

def altitude_padrao_voo_drone(relevo_regiao):

    if relevo_regiao == 'plano':
        return 100
    if relevo_regiao == 'morro':
        return 400

def test_altitude_padrao_voo_drone_mockado_com_contexto():

    with patch('test_patch_side_effect.altitude_padrao_voo_drone') as mock_func:
        mock_func.side_effect = [100, 400]

        assert mock_func('plano') == 100
        assert mock_func('morro') == 400

def test_altitude_padrao_voo_drone_mockado_sem_contexto(mocker):
    
    mocker.patch('test_patch_side_effect.altitude_padrao_voo_drone',
                side_effect = [100, 400]
    )
       
    assert altitude_padrao_voo_drone('plano') == 100
    assert altitude_padrao_voo_drone('morro') == 400

def test_altitude_padrao_voo_drone_mockado_com_return_value(mocker):

    mocker.patch('test_patch_side_effect.altitude_padrao_voo_drone',
                return_value = 400
    )

    assert altitude_padrao_voo_drone('morro') == 400


def test_altitude_padrao_voo_drone_mockado_lamda(mocker):
    
    mocker.patch('test_patch_side_effect.altitude_padrao_voo_drone',
                side_effect = lambda relevo_regiao: { 
                    
                    "plano": 100,
                    "morro": 400,
                }.get(relevo_regiao)
    )
       
    assert altitude_padrao_voo_drone('morro') == 400
    assert altitude_padrao_voo_drone('plano') == 100

    with pytest.raises(TypeError):

        assert altitude_padrao_voo_drone() == 100

