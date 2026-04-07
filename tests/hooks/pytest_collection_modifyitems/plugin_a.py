from pytest import hookimpl

@hookimpl(hookwrapper=True)
def pytest_collection_modifyitems(session, config, items):

    print("\n hookimpl(hookwrapper=True)-> Executa primeiro !")

    yield items

    print("hookimpl(hookwrapper=True) -> Executa por ultimo !")
