import pytest
from unittest.mock import Mock
from src.motor_drone import MotorDrone


def test_o_motor_deve_ser_ligado():

    mock_motor = Mock(spec=MotorDrone)

    mock_motor.ligar_motores.return_value = True
    mock_motor.ligar_motores()
    #mock_motor.ligar_motores() # O teste falha se chamar a função de ligar motores mais de uma vez

    mock_motor.ligar_motores.assert_called_once()