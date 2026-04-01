from pytest import fixture
from pytest_bdd import scenarios,given,when,then,parsers

scenarios("../features/bank_transactions_scenario_outline.feature")

@fixture
def account_balance():
    return {"balance":0}

@given(parsers.parse("the account balance is ${balance:d}"))
def account_initial_balance(account_balance,balance):
    account_balance["balance"] = balance

@when(parsers.parse("I deposit ${deposit:d}"))
def deposit(account_balance, deposit):
    account_balance["balance"] += deposit

@then(parsers.parse("the account balance should be ${new_balance:d}"))
def account_balance_should_be(account_balance,new_balance):
    account_balance["balance"] = new_balance
