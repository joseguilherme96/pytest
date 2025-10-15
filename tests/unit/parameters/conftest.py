from pytest import fixture

@fixture()
def calcular_peso_de_materia_prima(materia_prima_id:int,comprimento:int,largura:int,altura:int):

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

        return material["id_materia_prima"] == materia_prima_id

    materia_prima = list(filter(filtrar,materias_primas))[0]

    peso = (materia_prima["densidade"] * comprimento * largura * altura) / 10000000

    return peso
