from src.core import contruir_xml,validar_xml
import xml.etree.ElementTree as ET
from pytest import raises

def test_xml_transform():

    data = {"nome":"José Guilherme", "idade":29}
    xml_construido = contruir_xml(data)
    print(xml_construido)

    xml = ET.fromstring(xml_construido)
    assert xml.find('nome').text == 'José Guilherme'
    assert xml.find('idade').text == '29'

    esperado = """<?xml version="1.0" encoding="UTF-8"?>
    <registro>
        <nome>José Guilherme</nome>
        <idade>29</idade>
    </registro>"""
    assert xml_construido == esperado


def test_xml_deve_ser_invalido_devido_ao_nome_ser_invalido():

    xml_invalido = """<?xml version="1.0" encoding="UTF-8"?>
    <registro>
        <nome>s</nome>
        <idade>29</idade>
    </registro>"""

    xml = ET.fromstring(xml_invalido)

    with raises(Exception):

        validar_xml(xml)

def test_xml_deve_ser_invalido_devido_a_idade_ser_invalida():

    xml_invalido = """<?xml version="1.0" encoding="UTF-8"?>
    <registro>
        <nome>Jose Guilherme</nome>
        <idade>290</idade>
    </registro>"""

    xml = ET.fromstring(xml_invalido)

    with raises(Exception):

        validar_xml(xml)
       
