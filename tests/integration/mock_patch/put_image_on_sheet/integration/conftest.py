from pytest import fixture
from ..src.put_image_on_sheet import Imagem,Pdf
from unittest.mock import Mock

@fixture
def tmp_images(tmp_path):

    mock_imagem = Mock(spec=Imagem)

    img = tmp_path / "imagens"
    img.mkdir()
    imagens = []
    
    for x in range(0,30):

        img_path = img / f"{x}imagem.png"

        imagem = mock_imagem.gerar_imagem.return_value = img_path
        imagem = mock_imagem.gerar_imagem()
        imagens.append(imagem)

    yield imagens

@fixture
def tmp_pdf(tmp_path):

    path_pdf = tmp_path / "images_on_sheet"
    path_pdf.mkdir()
    path_pdf = path_pdf / "images_on_sheet.pdf"

    yield path_pdf

@fixture
def mock_imagens_convertidas(tmp_images):

    mock_imagem = Mock(spec=Imagem)

    mock_imagem.converter_imagens_para_comprimento_largura_maxima_de_acordo_com_a_quantidade_de_imagens_ser_colocada_na_folha.return_value = tmp_images
    imagens_convertidas = mock_imagem.converter_imagens_para_comprimento_largura_maxima_de_acordo_com_a_quantidade_de_imagens_ser_colocada_na_folha(tmp_images)

    yield imagens_convertidas
