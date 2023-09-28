from django.core.exceptions import PermissionDenied

def view_accounts(user):
    if user.has_perm('accounts.view_customuser'):
        return True
    else:
        raise PermissionDenied

def add_accounts(user):
    if user.has_perm('accounts.add_customuser'):
        return True
    else:
        raise PermissionDenied

def update_accounts(user):
    if user.has_perm('accounts.change_customuser'):
        return True
    else:
        raise PermissionDenied

def delete_accounts(user):
    if user.has_perm('accounts.delete_customuser'):
        return True
    else:
        raise PermissionDenied