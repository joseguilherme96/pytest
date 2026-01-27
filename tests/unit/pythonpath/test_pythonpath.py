import sys
from pytest import mark
from pathlib import Path

@mark.skipif(sys.platform != "win32", reason="Somente windows")
def test_deve_estar_definido_a_pasta_src_em_sys_path():

    caminhos = sys.path
    root_project = Path(__file__).resolve().parent.parent.parent.parent

    try:
        srcs = caminhos.index(f"{str(root_project)}\\src")
        assert True

    except:

        assert False