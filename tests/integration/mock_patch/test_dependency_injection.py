from abc import ABC, abstractmethod

def test_display_drone():

    mock_display_drone_formatter = DisplayDroneFormatter()

    distancia = Distancia(mock_display_drone_formatter)
    bateria = Bateria(mock_display_drone_formatter)

    distancia.distancia_alvo()
    bateria.carga()

    result = mock_display_drone_formatter.display_formatter()

    assert result == f""" Distância do alvo : {distancia.distancia_alvo()}m Bateria : {bateria.carga()}% """

class DisplayFormatter(ABC):

    @abstractmethod
    def display_formatter(self) -> str:
        pass

class DisplayDroneFormatter(DisplayFormatter):

    def __init__(self):

        self.informacoes = {}

    def display_formatter(self):

        return f""" Distância do alvo : {self.informacoes['distancia']}m Bateria : {self.informacoes['nivel_bateria']}% """

class Distancia:

    def __init__(self,display: DisplayFormatter):

        self.display = display

    def distancia_alvo(self):

        self.display.informacoes['distancia'] = 10
        return 10

class Bateria:

    def __init__(self,display: DisplayFormatter):

        self.display = display

    def carga(self):

        self.display.informacoes['nivel_bateria'] = 50
        return 50
    


