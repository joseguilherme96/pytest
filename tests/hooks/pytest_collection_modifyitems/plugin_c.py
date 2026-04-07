from pytest import hookimpl

@hookimpl(trylast=True)
def pytest_collection_modifyitems(session, config, items):

    print("Executa por penultimo !")
