def verify_account_owner(user, account):

    if user.id != account.owner:
        raise PermissionError("Unauthorized")

    return True