import subprocess,logging
from dotenv import load_dotenv
import os

load_dotenv()

def conectar_bd(CONFIG_BANCO_DADOS):

    host,user,password = CONFIG_BANCO_DADOS.values()

    logging.info(host)
    logging.info(user)
    logging.info(password)
    logging.info("Inciando conexão com Banco de dados.....")
    
    resultado = subprocess.run(f"mysqladmin ping -h {host} -u {user} -p {password}",shell=True,capture_output=True,text=True)
    
    if(resultado.returncode == 0):

        print(resultado.stdout)
        print("Banco conectado com sucesso !")

    if(resultado.returncode == 1):

        print(resultado.stderr)
        print("Falha ao conectar !")


def test_deve_conectar_ao_banco_de_dados(capsys):

    CONFIG_BANCO_DADOS = {

        "DB_HOST":os.getenv("DB_HOST"),
        "DB_USER":os.getenv("DB_USER"),
        "DB_PASSWORD":os.getenv("DB_PASSWORD")
    }

    conectar_bd(CONFIG_BANCO_DADOS)

    captured = capsys.readouterr()
    assert "Banco conectado com sucesso !" in captured.out

def test_deve_nao_conectar_ao_banco_de_dados(capsys):

    CONFIG_BANCO_DADOS = {

        "DB_HOST":os.getenv("DB_HOST"),
        "DB_USER":os.getenv("DB_USER"),
        "DB_PASSWORD":"aaa"
    }

    conectar_bd(CONFIG_BANCO_DADOS)

    captured = capsys.readouterr()
    assert "Falha ao conectar !\n" in captured.out



