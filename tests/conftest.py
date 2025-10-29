from pytest import fixture
from dynaconf import settings

@fixture(scope="session",autouse=True)
def set_test_settigs():

    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
    print("\n🌱 Ambiente Dynaconf: TESTING ativado\n")

    