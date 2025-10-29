import pytest
import os

def remove():

    os.remove("wwww.dd")



def test_remove(mocker):

    mocker.patch("os.remove",side_effect=FileNotFoundError)

    with pytest.raises(FileNotFoundError):

        remove()

    