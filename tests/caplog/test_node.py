import subprocess,logging

def get_versao_node():

    resultado = subprocess.run(
        "node --version",
        capture_output=True,
        text=True 
    )
    print(resultado.stdout)


def test_node_deve_estar_instalado(capsys):

    get_versao_node()

    capture = capsys.readouterr()

    assert capture.out.strip() != ""