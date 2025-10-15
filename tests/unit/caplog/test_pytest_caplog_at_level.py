import logging


def ligar_motores_drone():

    logging.error("Falha ao ligar motor 1")
    logging.info("Motor dois ligado com sucesso !")
    logging.warning("Atenção motor já atingiu sua vida util !")
    logging.error("Falhas no motor 3 !")

def test_dois_motores_devem_apresentar_falhas_em_dois_motores(caplog):

    caplog.set_level(logging.ERROR)

    ligar_motores_drone()

    errors = [r for r in caplog.records if r.levelno == logging.ERROR]
    assert len(errors) == 2


