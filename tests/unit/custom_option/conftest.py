def pytest_addoption(parser):

    parser.addoption("--custom-option", action="store", default="default_value", help="Description of the custom option.")
