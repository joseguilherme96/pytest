import os
from dotenv import load_dotenv
import env

def test_env():
    assert os.getenv("DB_HOST") == 'LOCALHOST'

def test_env_py():

    assert os.getenv("PASTA_USER") == 'user'
    assert os.environ['PASTA_USER'] == 'user'

def test_env_pytest_ini():

    assert os.environ["DEPLOYMENT_STAGE"] == "staging"
    assert os.environ["API_ENDPOINT"] == "https://api.staging.example.com"
    assert os.environ["ACCOUNT_ID"] == "56789"

# O teste foi comentada para não dar conflito com as variaveis de ambiente já definidas no pytest.ini e com o teste acima.
# def test_variavel_ambiente_em_arquivo_com_extensao_toml():

#     load_dotenv()
#     assert os.getenv("PASTA_RECEBIMENTO")  == "received"
#     assert os.getenv("PASTA_PROCESSO")  == "process"
#     assert os.getenv("PASTA_PROCESSADO")  == "processed"


