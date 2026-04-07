from pytest import hookimpl

@hookimpl(tryfirst=True)
def pytest_collection_modifyitems(session, config, items):

    print("Executa por segundo !")

