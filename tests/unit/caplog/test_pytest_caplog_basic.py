import logging

def ligar_drone():

    logging.info(f"Drone ligado !")

def test_logs_correct_nome_drone(caplog):
    caplog.set_level(logging.INFO)
    ligar_drone()
    assert "Drone ligado !" in caplog.text