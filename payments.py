def process_payment(account, amount):

    if amount <= 0:
        raise ValueError("Payment must be positive")

    if amount > account.balance:
        raise ValueError("Insufficient funds")

    account.balance -= amount

    return account.balance