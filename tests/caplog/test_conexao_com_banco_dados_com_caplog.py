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

        logging.info("Banco conectado com sucesso !")
        logging.info(resultado.stdout)

    if(resultado.returncode == 1):

        logging.error("Falha ao conectar !")
        logging.info(resultado.stderr)



def test_deve_conectar_ao_banco_de_dados(caplog):

    caplog.set_level(logging.INFO)

    CONFIG_BANCO_DADOS = {

        "DB_HOST":os.getenv("DB_HOST"),
        "DB_USER":os.getenv("DB_USER"),
        "DB_PASSWORD":os.getenv("DB_PASSWORD")
    }

    conectar_bd(CONFIG_BANCO_DADOS)

    assert "Inciando conexão com Banco de dados....." in caplog.text
    assert "Banco conectado com sucesso !" in caplog.text
    assert "mysqld is alive\n" in caplog.text

    caplog.clear()

def test_deve_nao_conectar_ao_banco_de_dados(caplog):

    caplog.set_level(logging.INFO)

    CONFIG_BANCO_DADOS = {

        "DB_HOST":os.getenv("DB_HOST"),
        "DB_USER":os.getenv("DB_USER"),
        "DB_PASSWORD":'aaa'
    }

    conectar_bd(CONFIG_BANCO_DADOS)

    assert "Falha ao conectar !" in caplog.text

