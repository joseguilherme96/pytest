from pytest import hookimpl,CallInfo


@hookimpl()
def pytest_runtest_makereport(item, call: CallInfo):
    print()

    if call.when == "setup":

        print("SETUP dos testes")

    if call.when == "call":
        print("Hello from `pytest_runtest_makereport` execution")
        print("  -> test execution")

        outcome = call.excinfo

        try:

            test_outcome = "failed" if outcome else "passed"
            test_duration = call.duration
            test_id = item.nodeid

            print(f"Test: {test_id} ")
            print(f"Outcome: {test_outcome}")
            print(f"Duration: {test_duration}")

        except Exception as e:
            print(f"Error: {e}")

    if call.when == "teardown":

        print("TEAR DOWN")
