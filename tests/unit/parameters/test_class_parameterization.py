from pytest import mark
from src.class_parameterization import MateriaPrimaPeso


@mark.parametrize("materia_prima_id,comprimento,largura,altura,esperado",
    [

        (1,100,100,50,0.135),
        (2,500,500,50,9.8375)
                      
],)
class TestMateriaPrimaPeso:

    def test_deve_calcular_corretamente_o_peso_da_materia_prima_de_acordo_com_suas_dimensoes_e_a_materia_prima_id(self,materia_prima_id,comprimento,largura,altura,esperado):

        materia_prima_peso = MateriaPrimaPeso(materia_prima_id,comprimento,largura,altura)
        assert materia_prima_peso.calcular_peso_de_materia_prima() == esperado
