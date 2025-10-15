def test_criar_arquivo_csv(tmp_path):

    temp_dir = tmp_path / "arquivos_csv"
    temp_dir.mkdir()

    temp_file = temp_dir /  "plantas_usadas_em_comesticos.csv"
    temp_file.write_text(""" 

    nome;descricao;
    Açai;rico em antioxidantes, usado em cremes, máscaras e sucos;
    Cúrcuma;ação anti-inflamatória, antisséptica e clareadora;
    Gengibre;estimulante, circulatório, antioxidante.;
    Babosa (Aloe vera); hidratante, calmante em queimaduras / pós-sol;                                   
    """)

    assert temp_file.is_file()

