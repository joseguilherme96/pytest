class MateriaPrimaPeso:

    def __init__(self,materia_prima_id:int,comprimento:int,largura:int,altura:int)->None:
        
        self.materia_prima_id = materia_prima_id
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura

    def calcular_peso_de_materia_prima(self):

        materias_primas = [

            {
                "id_materia_prima":1,
                "material":"Alumínio(Al)",
                "densidade":2.70
            },
            {
                "id_materia_prima":2,
                "material":"Ferro(Fe)",
                "densidade":7.87
            }
        ]

        def filtrar(material):

            return material["id_materia_prima"] == self.materia_prima_id

        materia_prima = list(filter(filtrar,materias_primas))[0]

        peso = (materia_prima["densidade"] * self.comprimento * self.largura * self.altura) / 10000000

        return peso
