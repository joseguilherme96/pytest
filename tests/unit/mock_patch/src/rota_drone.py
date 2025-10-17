
import requests

class RotaDrone:

    def __init__(self,api_url):

        self.api_url = api_url

    def get_rota(self,endereco_origem,endereco_destino):

        response = requests.post(f"{self.api_url}/rota",json={"endereco_origem":endereco_origem,"endereco_destino":endereco_destino})

        return response.json()