import os
from dotenv import load_dotenv
import env
from pytest import mark

def test_env():
    assert os.getenv("DB_HOST") == 'LOCALHOST'

def test_env_py():

    assert os.getenv("PASTA_USER") == 'user'
    assert os.environ['PASTA_USER'] == 'user'

def test_env_pytest_ini():

    assert os.environ["DEPLOYMENT_STAGE"] == "staging"
    assert os.environ["API_ENDPOINT"] == "https://api.staging.example.com"
    assert os.environ["ACCOUNT_ID"] == "56789"


@mark.skip(reason="O teste está desativado para não dar conflito, pois as variaveis de ambiente estão definidas no pytest.ini. " \
"O teste seria válido se as variaveis de ambiente estivessem sendo definidas no arquivo no arquivo pyproject.toml." \
"E o teste acima teria que ser desativado para evitar conflito !")
def test_variavel_ambiente_em_arquivo_com_extensao_toml():

    load_dotenv()
    assert os.getenv("PASTA_RECEBIMENTO")  == "received"
    assert os.getenv("PASTA_PROCESSO")  == "process"
    assert os.getenv("PASTA_PROCESSADO")  == "processed"


