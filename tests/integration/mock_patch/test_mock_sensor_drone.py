from unittest.mock import Mock
from src.implementacao_conceitual_drone_para_teste_mock import FakeBateria,PilotagemDrone,FakeSensor,FakeSensores,FakeMotor
import logging

def test_drone_deve_subir_ate_atingir_distancia_minima_de_30_centimetros_entre_a_parte_superior_drone_com_o_alvo(caplog):

    caplog.set_level(logging.INFO)
    bateria = FakeBateria()

    sensor_distancia = Mock(spec = FakeSensores(*[FakeSensor() for x in range(0,6)]))

    for distancia_entre_o_alvo_e_o_drone in (range(100,20,-10)):

        sensor_distancia.get_distancias_entre_os_sensores_e_os_alvos.return_value = [100,100,100,100,distancia_entre_o_alvo_e_o_drone,100]
        pilotagem_drone = PilotagemDrone(sensor_distancia,FakeMotor(),bateria)

        assert pilotagem_drone.subir() == True
