from pytest import mark
from src.function_parameterization import calcular_peso_de_materia_prima

def calcular_peso_de_materia_prima_esperado(materia_prima_id:int,comprimento:int,largura:int,altura:int):

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

@mark.parametrize("materia_prima_id", [1, 2])
@mark.parametrize("altura", [50, 100])
@mark.parametrize("largura", [100, 200])
@mark.parametrize("comprimento", [100, 200])
def test_deve_calcular_corretamente_o_peso_da_materia_prima_de_acordo_com_suas_dimensoes_e_a_materia_prima_id_combinado(materia_prima_id, altura, largura, comprimento):
    esperado = calcular_peso_de_materia_prima_esperado(materia_prima_id, comprimento, largura, altura)

    resultado = calcular_peso_de_materia_prima(materia_prima_id, comprimento, largura, altura)

    print(f"ID Matéria Prima: {materia_prima_id}, Altura: {altura}, Largura: {largura}, Comprimento: {comprimento}, Peso Esperado: {esperado}")
    assert resultado == esperado
