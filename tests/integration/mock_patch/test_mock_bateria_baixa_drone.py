from unittest.mock import Mock
from src.implementacao_conceitual_drone_para_teste_mock import FakeBateria,PilotagemDrone,FakeSensor,FakeSensores,FakeMotor
import logging

def test_com_mock_drone_nao_deve_subir_porque_a_bateria_nao_esta_com_apenas_10_porcento_da_sua_capacidade(caplog):

    caplog.set_level(logging.INFO)
    bateria = Mock(autospec = FakeBateria)
    bateria.carga.return_value = 10

    sensor_distancia = FakeSensores(*[FakeSensor() for x in range(0,6)])
    direcao_drone = PilotagemDrone(sensor_distancia,FakeMotor(),bateria)
    direcao_drone.subir()

    assert direcao_drone.subir() == False

def test_com_mock_deve_subir_ate_a_bateria_estiver_com_apenas_11_porcento_da_sua_capacidade(caplog):

    caplog.set_level(logging.INFO)
    bateria = Mock(autospec = FakeBateria)
    sensor_distancia = (Mock(autospec = FakeSensores(*[FakeSensor() for x in range(0,6)])))
    sensor_distancia.get_distancias_entre_os_sensores_e_os_alvos.return_value = [50,50,50,50,50,50]

    for carga in range(50,11,-1):

        bateria.carga.return_value = carga
        direcao_drone = PilotagemDrone(sensor_distancia,FakeMotor(),bateria)
        
        assert direcao_drone.subir() == True
