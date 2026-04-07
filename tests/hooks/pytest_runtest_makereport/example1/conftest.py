from pytest import hookimpl


@hookimpl()
def pytest_sessionstart(session):
    print("Hello from `pytest_sessionstart` hook!")

@hookimpl()
def pytest_sessionfinish(session, exitstatus):
    print()
    print("Hello from `pytest_sessionfinish` hook!")
    print(f"Exit status: {exitstatus}")


