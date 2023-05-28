import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(100)

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (7, 1, 8),
    (10, 10, 20),
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(3, 2) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2


def test_bank_set_initial_balance(bank_account):
    assert bank_account.balance == 100

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(50)
    assert bank_account.balance == 50

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance == 150

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 110


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (100, 50, 50),
    (300, 200, 100),
    (100, 100, 0)
])
def test_bank_transactions(deposited, withdrew, expected, zero_bank_account):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)

