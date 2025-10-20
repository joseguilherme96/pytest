import logging

class ConfigurarDrone:

    def definir_rota(self):

        return True
    
    def definir_tempo_de_voo(self):

        return True
    
    def definir_distancia(self):

        return True
    
    def definir_altura_maxima(self):

        return True
    
class VerificarDrone:

    def __init__(self):
        pass

    def verificar_motores(self):

        return True

    def verificar_rota(self):

        return True
    
    def verificar_sensor_de_distancia(self):

        return True

    def verificar_distancia(self):

        return True
    
    def verificar_altura_maxima(self):

        return True
    
    def verificar_autonomia_bateria(self):

        return True
    
    def verificar_camera(self):

        return True
    
class FakeLigarDrone:

    def __init__(self,motor):
        self.motor = motor

    def ligar(self):

        logging.info("Ligando drone !")

        if not self.motor.ligar_motores():

            return False
        
        if not self.ligar_luzes():

            return False
        
        if not self.ligar_camera():

            return False

        return True
    
    def ligar_luzes(self):

        return True
    
    def ligar_camera(self):

        return True
 
class FakeBateria:

    def __init__(self,bateria=None):

        self.bateria = bateria

    def carga(self):

        return 100
   
class FakeMotor:

    def __init__(self,motor=None):

        self.power = 0
        self.motor = motor

    def ligar_motores(self):

        return True
    
    def acelerar(self):

        return True
    
    def desacelerar(self):

        return True
    
    def manter_aceleracao(self):

        return True
    
class FakeSensor:

    def __init__(self,sensor=None):

        self.distancia = 50
        self.sensor = sensor

    def get_distancia_entre_o_drone_e_o_alvo(self):

        return 100
    
class FakeSensores:

    def __init__(self,sensor_frontal,sensor_traseiro,sensor_lateral_esquerda,sensor_lateral_direita,sensor_em_cima,sensor_em_baixo):
        
        self.sensor_frontal = sensor_frontal
        self.sensor_traseiro = sensor_traseiro
        self.sensor_lateral_esquerda = sensor_lateral_esquerda
        self.sensor_lateral_direita = sensor_lateral_direita
        self.sensor_em_baixo = sensor_em_baixo
        self.sensor_em_cima = sensor_em_cima

    def get_distancias_entre_os_sensores_e_os_alvos(self):

        sensores = list(self.__dict__)

        distancias = []

        for sensor in sensores:

            distancia_sensor_entre_o_drone_e_o_alvo = self.__dict__[sensor].get_distancia_entre_o_drone_e_o_alvo()

            distancias.append(distancia_sensor_entre_o_drone_e_o_alvo)

        logging.info(f"Distância entre o drone e o alvo : {distancias}")

        return distancias

class PilotagemDrone:

    def __init__(self,sensor_distancia,motor,bateria):

        self.sensor_distancia = sensor_distancia
        self.motor = motor
        self.altitude = 0
        self.bateria = bateria

    def subir(self):

        distancia = self.sensor_distancia.get_distancias_entre_os_sensores_e_os_alvos()[4]

        if self.bateria.carga() <= 10:

            self.descer()
            return False

        if distancia < 30:

            self.parar()
            return False
        
        self.motor.acelerar()
        self.altitude +=10
        logging.info("Subindo drone...")
        logging.info(f"Altitude: {self.altitude}")

        return True
    
    def descer(self):

        self.motor.desacelerar()
        return True
    
    def direita(self):

        return True
    
    def esquerda(self):

        return True
    
    def girar(self):

        return True
    
    def avancar(self):

        return True
    
    def recuar(self):

        return True
    
    def parar(self):

        logging.info("Drone parado...")
        return True

class Voo:

    def __init__(self,ligar_drone,verificar_drone,direcao_drone):
        
        self.ligar_drone = ligar_drone
        self.verificar_drone = verificar_drone
        self.direcao_drone = direcao_drone

    def voar(self):

        if not self.ligar_drone.ligar():

            logging.error("Falha ao ligar Drone...")

            return False

        logging.info("Drone ligado...")

        while True:
            
            if not self.direcao_drone.subir():
                break

### Exemplo de uso ###

# sensor_distancia =  FakeSensores(*[FakeSensor() for x in range(0,6)])
# motor = FakeMotor()
# bateria = FakeBateria()
# direcao = PilotagemDrone(sensor_distancia,motor,bateria)
# ligar_drone = FakeLigarDrone(motor)
# verificar_drone = VerificarDrone()

# voo = Voo(ligar_drone,verificar_drone,direcao)
# voo.voar()