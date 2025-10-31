import subprocess,logging
from dotenv import load_dotenv
import os
from pytest import mark

load_dotenv()

@mark.testdb
def conectar_bd(CONFIG_BANCO_DADOS):

    host,user,password = CONFIG_BANCO_DADOS.values()

    logging.info(host)
    logging.info(user)
    logging.info(password)
    logging.info("Inciando conexão com Banco de dados.....")
    
    resultado = subprocess.run(f"mysqladmin ping -h {host} -u {user} --password={password}",shell=True,capture_output=True,text=True)

    logging.info(resultado.returncode)
    
    if(resultado.returncode == 0 and "alive" in resultado.stdout):

        print(resultado.stdout)
        print("Banco conectado com sucesso !")

    else:

        print(resultado.stderr)
        print("Falha ao conectar !")

@mark.testdb
def test_deve_conectar_ao_banco_de_dados(capsys):

    CONFIG_BANCO_DADOS = {

        "DB_HOST":os.getenv("DB_HOST"),
        "DB_USER":os.getenv("DB_USER"),
        "DB_PASSWORD":os.getenv("DB_PASSWORD")
    }

    conectar_bd(CONFIG_BANCO_DADOS)

    captured = capsys.readouterr()
    assert "Banco conectado com sucesso !" in captured.out

@mark.testdb
def test_deve_nao_conectar_ao_banco_de_dados(caplog,capsys):

    caplog.set_level(logging.INFO)

    CONFIG_BANCO_DADOS = {

        "DB_HOST":os.getenv("DB_HOST"),
        "DB_USER":os.getenv("DB_USER"),
        "DB_PASSWORD":"aaa"
    }

    conectar_bd(CONFIG_BANCO_DADOS)

    captured = capsys.readouterr()
    assert "Falha ao conectar !\n" in captured.out



