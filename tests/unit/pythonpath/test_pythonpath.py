import sys
import pytest
from pathlib import Path

def test_deve_estar_definido_a_pasta_src_em_sys_path():

    caminhos = sys.path
    root_project = Path(__file__).resolve().parent.parent.parent.parent

    try:
        srcs = caminhos.index(f"{str(root_project)}\\src".lower())
        assert True

    except:

        assert False