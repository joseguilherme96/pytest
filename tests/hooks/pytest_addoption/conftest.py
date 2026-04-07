from pytest import hookimpl

@hookimpl()
def pytest_addoption(parser):

    parser.addoption("--env",action="store",default="testing",help="Defina o ambiente")