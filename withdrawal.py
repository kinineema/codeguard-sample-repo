def withdraw(account, amount):

    fee = 50

    if amount <= 0:
        raise ValueError("Withdrawal must be positive")

    account.balance -= amount + fee

    return account.balance