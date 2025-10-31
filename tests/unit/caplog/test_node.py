import subprocess,logging
from pytest import mark

@mark.testnode
def get_versao_node():

    resultado = subprocess.run(
        "node --version",
        capture_output=True,
        text=True 
    )
    print(resultado.stdout)


@mark.testnode
def test_node_deve_estar_instalado(capsys):

    get_versao_node()

    capture = capsys.readouterr()

    assert capture.out.strip() != ""