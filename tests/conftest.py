from pytest import fixture
from dynaconf import settings

@fixture(scope="session",autouse=True)
def set_test_settigs():

    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
    print("\n🌱 Ambiente Dynaconf: TESTING ativado\n")

pytest_plugins = (
    "hooks.pytest_collection_modifyitems.plugin_b",
    "hooks.pytest_collection_modifyitems.plugin_a",
    "hooks.pytest_collection_modifyitems.plugin_c"
)

    