def contruir_xml(data: object):

    template_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <registro>
        <nome>{nome}</nome>
        <idade>{idade}</idade>
    </registro>"""

    xml = template_xml.format(nome=data.get("nome"), idade=data.get("idade"))

    return xml

def validar_xml(xml: object):

    try:

        nome = xml.find("nome").text
        idade = int(xml.find("idade").text)

        if len(nome) < 10 or len(nome) > 50:
            
            raise Exception("Nome invalido!")
        
        if int(idade) < 18 or idade > 150:

            raise Exception("idade invalida!")
    
    except Exception as e :

        raise e
