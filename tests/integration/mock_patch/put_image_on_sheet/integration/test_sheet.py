from ..src.put_image_on_sheet import Folha,FolhaImagem
from pytest import mark

@mark.parametrize("quantidade_de_imagens_por_folha, comprimento_maximo_esperado_imagem,largura_maxima_esperada_imagem",
                  [
                      (3,118.5,75),
                      (5,79,75),
                      (6,79,75)
                  ],)
def test_deve_retornar_dimensoes_maximas_que_a_imagem_pode_ser_colocada_na_folha(quantidade_de_imagens_por_folha,comprimento_maximo_esperado_imagem,largura_maxima_esperada_imagem):

    folha = Folha(tipo_folha="A4",comprimento=210,largura=297,margem_em_cada_lado=30)

    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=quantidade_de_imagens_por_folha)

    comprimento,largura = folha_imagem.calcular_dimensao_comprimento_largura_maxima_de_cada_imagem_de_acordo_com_a_quantidade_de_imagens_ser_colocada_na_folha()

    assert comprimento == comprimento_maximo_esperado_imagem
    assert largura == largura_maxima_esperada_imagem

@mark.parametrize("quantidade_de_imagens_por_folha, quantidade_linhas_esperado,quantidade_colunas_esperadas",
                  [
                      (3,2,2),
                      (5,3,2),
                      (6,3,2)
                  ],)
def test_deve_retornar_a_quantidade_de_linhas_colunas_que_a_folha_tera_para_inserir_as_imagens(quantidade_de_imagens_por_folha,quantidade_linhas_esperado,quantidade_colunas_esperadas):

    folha = Folha(tipo_folha="A4",comprimento=210,largura=297,margem_em_cada_lado=30)

    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=quantidade_de_imagens_por_folha)

    quantidade_linhas,quantidade_colunas = folha_imagem.criar_linhas_colunas_para_inserir_imagens()

    assert quantidade_linhas == quantidade_linhas_esperado
    assert quantidade_colunas == quantidade_colunas_esperadas

