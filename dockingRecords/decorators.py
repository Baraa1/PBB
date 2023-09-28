from django.core.exceptions import PermissionDenied

def view_records(user):
    if user.has_perm('dockingRecords.view_dockingrecord'):
        return True
    else:
        raise PermissionDenied

def add_records(user):
    if user.has_perm('dockingRecords.add_dockingrecord'):
        return True
    else:
        raise PermissionDenied

def update_records(user):
    if user.has_perm('dockingRecords.change_dockingrecord'):
        return True
    else:
        raise PermissionDenied

def delete_records(user):
    if user.has_perm('dockingRecords.delete_dockingrecord'):
        return True
    else:
        raise PermissionDenied
