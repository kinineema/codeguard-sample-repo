def withdraw(account, amount):

    fee = 50

    account.balance -= amount + fee

    return account.balance