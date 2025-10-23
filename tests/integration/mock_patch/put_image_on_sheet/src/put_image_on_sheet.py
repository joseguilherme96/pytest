import math
from pathlib import Path

class Folha:

    def __init__(self,tipo_folha: str,comprimento:int,largura:int,margem_em_cada_lado:int):

        self.tipo_folha = tipo_folha
        self.comprimento = comprimento
        self.largura = largura
        self.margem_em_cada_lado = margem_em_cada_lado
        self.area_livre = None
        self.comprimento_livre = None
        self.largura_livre = None

    def calcular_area_livre(self):

        somatoria_margin_dois_lados = self.margem_em_cada_lado * 2
        self.area_livre = ((self.comprimento - somatoria_margin_dois_lados) * ( self.largura - somatoria_margin_dois_lados))

        return self.area_livre
    
    def calcular_largura_livre(self):

        somatoria_margin_dois_lados = self.margem_em_cada_lado * 2
        self.largura_livre = self.largura - somatoria_margin_dois_lados

        return self.largura_livre
    
    def calcular_comprimento_livre(self):

        somatoria_margin_dois_lados = self.margem_em_cada_lado * 2
        self.comprimento_livre = self.comprimento - somatoria_margin_dois_lados

        return self.comprimento_livre

class FolhaImagem:

    def __init__(self,folha,quantidade_imagens_por_folha):

        self.folha = folha
        self.quantidade_imagens_por_folha = quantidade_imagens_por_folha
        self.quantidade_linhas = None
        self.quantidade_colunas = None
        self.comprimento_maximo_imagem_na_folha : None
        self.largura_maxima_imagem_na_folha : None

    def calcular_dimensao_comprimento_largura_maxima_de_cada_imagem_de_acordo_com_a_quantidade_de_imagens_ser_colocada_na_folha(self):

        self.criar_linhas_colunas_para_inserir_imagens()

        comprimento_imagem = self.folha.calcular_largura_livre() / self.quantidade_linhas
        largura_imagem = self.folha.calcular_comprimento_livre() / self.quantidade_colunas

        self.comprimento_maximo_imagem_na_folha = comprimento_imagem
        self.largura_maxima_imagem_na_folha = largura_imagem

        return [comprimento_imagem,largura_imagem]
    
    def criar_linhas_colunas_para_inserir_imagens(self):

        self.quantidade_linhas = math.ceil(math.sqrt(self.quantidade_imagens_por_folha))
        self.quantidade_colunas = math.ceil(self.quantidade_imagens_por_folha / self.quantidade_linhas)

        return [self.quantidade_linhas,self.quantidade_colunas]

        

class MockImagem:

    pass

class Imagem:

    def __init__(self,imagem,folha_imagem):

        self.imagem = imagem
        self.folha_imagem = folha_imagem

    def gerar_imagem():

        return True
    
    def converter_imagens_para_comprimento_largura_maxima_de_acordo_com_a_quantidade_de_imagens_ser_colocada_na_folha(self,imagens:list):

        return []

class MockPdf:

    pass

class Pdf:

    def __init__(self,pdf):

        self.pdf = pdf

    def criar_pdf_com_imagens(self,imagens):

        return Path
    

def main():

    
    folha = Folha(tipo_folha='A4',comprimento=210,largura=297,margem=10)
    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=6)
    imagens = Imagem(MockImagem,folha_imagem)
    pdf = Pdf(MockPdf)

    imagens = imagens.converter_imagens_para_comprimento_largura_maxima_de_acordo_com_a_quantidade_de_imagens_ser_colocada_na_folha([])
    criar_pdf_com_imagens = pdf.criar_pdf_com_imagens(imagens,folha_imagem.quantidade_imagens_por_folha)

    return True

if __name__ == 'main':

    main()

    

