from pytest import mark

@mark.parametrize("materia_prima_id,comprimento,largura,altura,esperado",
    [

        (1,100,100,50,0.135),
        (2,500,500,50,9.8375)
                      
    ],)
def test_deve_calcular_corretamente_o_peso_da_materia_prima_de_acordo_com_suas_dimensoes_e_a_materia_prima_id(calcular_peso_de_materia_prima,materia_prima_id,comprimento,largura,altura,esperado):

    assert calcular_peso_de_materia_prima == esperado

