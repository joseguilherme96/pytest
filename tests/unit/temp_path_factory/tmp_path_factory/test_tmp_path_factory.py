def test_o_arquivo_deve_conter_5_linhas(criar_arquivo_compartilhado):

    with open(str(criar_arquivo_compartilhado),'r') as arquivo:

        assert len(arquivo.readlines()) == 5

    
def test_o_arquivo_deve_ter_colunas_padronizadas(criar_arquivo_compartilhado):

    with open(str(criar_arquivo_compartilhado),'r') as arquivo:

        colunas = arquivo.readline().split(";")

        assert ['nome','descricao','\n'] == colunas

def test_o_arquivo_deve_ser_na_extensao_csv(criar_arquivo_compartilhado):

    assert criar_arquivo_compartilhado.name.split(".")[1] == 'csv'
    

    