import logging

def levantar_drone():

    logging.info("Subir drone !")
    logging.warning("Permanecer por cinco 5s !")
    logging.info("Descer drone !")

def test_function_logs_caplog_messages(caplog):
    """Testing the caplog.messages attribute"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    levantar_drone()
    assert caplog.messages == ["Subir drone !", "Permanecer por cinco 5s !", "Descer drone !"]

def test_function_logs_caplog_text(caplog):
    """Testing the caplog.text attribute"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    levantar_drone()
    assert "Subir drone !" in caplog.text
    assert "Permanecer por cinco 5s !" in caplog.text
    assert "Descer drone !" in caplog.text

def test_function_logs_caplog_record_tuples(caplog):
    """Testing the caplog.record_tuples attribute"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    levantar_drone()
    assert caplog.record_tuples == [
        ("root", logging.INFO, "Subir drone !"),
        ("root", logging.WARNING, "Permanecer por cinco 5s !"),
        ("root", logging.INFO, "Descer drone !"),
    ]

def test_function_logs_caplog_records(caplog):
    """Testing the caplog.records attribute"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    levantar_drone()
    assert len(caplog.records) == 3
    assert caplog.records[0].message == "Subir drone !"
    assert caplog.records[1].message == "Permanecer por cinco 5s !"
    assert caplog.records[2].message == "Descer drone !"

def test_function_logs_caplog_clear(caplog):
    """Testing the caplog.clear() method"""
    caplog.set_level(logging.INFO)  # Set the caplog level to INFO and above
    levantar_drone()
    assert len(caplog.records) == 3
    caplog.clear()
    assert len(caplog.records) == 0