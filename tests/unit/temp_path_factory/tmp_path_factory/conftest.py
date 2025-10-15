from pytest import fixture
import os

@fixture(scope="session")
def criar_arquivo_compartilhado(tmp_path_factory):

    print("Cria arquivo !")

    temp_dir = tmp_path_factory.mktemp("data") / "arquivos_csv_compartilhado.csv"

    temp_dir.write_text("""nome;descricao;
    Açai;rico em antioxidantes, usado em cremes, máscaras e sucos;
    Cúrcuma;ação anti-inflamatória, antisséptica e clareadora;
    Gengibre;estimulante, circulatório, antioxidante.;
    Babosa (Aloe vera); hidratante, calmante em queimaduras / pós-sol;""")

    yield temp_dir  

    print("Remove arquivo !")  
    os.remove(temp_dir)
