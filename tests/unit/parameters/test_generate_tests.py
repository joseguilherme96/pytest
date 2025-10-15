from src.calcular_valor_total_produto import get_taxa_desconto_produto_por_categoria_id

def pytest_generate_tests(metafunc):

    if "categoria_id_1" in metafunc.fixturenames:

        metafunc.parametrize('produto_id,categoria_id_1,quatidade_max_permitida,esperado',[
            (1,1,10,0.05),
            (1,1,20,0.05),
            (1,1,5,0.05),
            (1,1,15,0.05),
        ])

    elif "categoria_id_2" in metafunc.fixturenames:

        metafunc.parametrize('produto_id,categoria_id_2,quatidade_max_permitida,esperado',[
            (2,2,2,0.1),
            (3,2,2,0.1),
            (4,2,2,0.1),
            (5,2,2,0.1),
        ])
        
        

def test_produto_da_categoria_id_1_deve_ter_taxa_de_5_por_cento_de_desconto(produto_id,categoria_id_1,quatidade_max_permitida,esperado):

    assert esperado == get_taxa_desconto_produto_por_categoria_id(categoria_id_1)

def test_produto_da_categoria_id_2_deve_ter_taxa_de_10_por_cento_de_desconto(produto_id,categoria_id_2,quatidade_max_permitida,esperado):

    assert esperado == get_taxa_desconto_produto_por_categoria_id(categoria_id_2)

