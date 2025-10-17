from unittest.mock import patch
from src.rota_drone import RotaDrone


@patch("src.rota_drone.requests.post")
def test_rota(mock_request_post):

    mock_request_post.return_value.json.return_value = [
        {
            "latitude":39394,
            "longitude":39348,
            "altitude":949494,
        },
        {
            "latitude":39394,
            "longitude":39348,
            "altitude":949494,
        }
    ]

    rota = RotaDrone("https://fakerota.com")
    result = rota.get_rota(endereco_origem="Rua das Flores, Nº 10 - Jardim Dos Ipês - Campinas - SP",endereco_destino="Rua das Pedras, Nº 5, Jardim Florenca, Campinas - SP")

    assert result == [
        {
            "latitude":39394,
            "longitude":39348,
            "altitude":949494,
        },
        {
            "latitude":39394,
            "longitude":39348,
            "altitude":949494,
        }
    ]
    mock_request_post.assert_called_once_with("https://fakerota.com/rota",json = {"endereco_origem":"Rua das Flores, Nº 10 - Jardim Dos Ipês - Campinas - SP","endereco_destino":"Rua das Pedras, Nº 5, Jardim Florenca, Campinas - SP"})