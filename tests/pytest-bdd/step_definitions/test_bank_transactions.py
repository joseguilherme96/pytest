from pytest import fixture
from pytest_bdd import scenarios, given, when, then

scenarios("../features/bank_transactions.feature")


@fixture
def account_balance():
    return {"balance":100}

@given('the account balance is $100')
def account_initial_balance(account_balance):
    account_balance["balance"] = 100

@when("I deposit $20")
def deposit(account_balance):
    account_balance["balance"] += 20

@then("the account balance should be $120")
def account_balance_should_be(account_balance):
    assert account_balance["balance"] == 120
