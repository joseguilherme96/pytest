def test_pytest_addoption(request):

    assert request.config.getoption("env") == "testing"