from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers


scenarios("../features/bank_transactions_param.feature")

@fixture
def account_balance():
    return {"balance":0}

@given(parsers.parse('the account balance is $"{balance:d}"'))
def account_initial_balance(account_balance, balance):
    account_balance["balance"] = balance

@when(parsers.parse('I deposit $"{deposit:d}"'))
def deposit(account_balance, deposit):
    account_balance["balance"] += deposit

@when(parsers.parse('I withdraw $"{withdrawal:d}"'))
def withdraw(account_balance, withdrawal):
    account_balance["balance"] -= withdrawal

@then(parsers.parse('the account balance should be $"{new_balance:d}"'))
def account_balance_should_be(account_balance, new_balance):
    assert account_balance["balance"] == new_balance



    





