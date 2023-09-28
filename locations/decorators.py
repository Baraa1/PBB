from django.core.exceptions import PermissionDenied

################################################################################################################################################################################
############################################################################# Terminals ########################################################################################
################################################################################################################################################################################

def view_terminals(user):
    if user.has_perm('locations.view_terminal'):
        return True
    else:
        raise PermissionDenied

def add_terminals(user):
    if user.has_perm('locations.add_terminal'):
        return True
    else:
        raise PermissionDenied

def update_terminals(user):
    if user.has_perm('locations.change_terminal'):
        return True
    else:
        raise PermissionDenied

def delete_terminals(user):
    if user.has_perm('locations.delete_terminal'):
        return True
    else:
        raise PermissionDenied

################################################################################################################################################################################
################################################################################# Gates ########################################################################################
################################################################################################################################################################################

def view_gates(user):
    if user.has_perm('locations.view_gate'):
        return True
    else:
        raise PermissionDenied

def add_gates(user):
    if user.has_perm('locations.add_gate'):
        return True
    else:
        raise PermissionDenied

def update_gates(user):
    if user.has_perm('locations.change_gate'):
        return True
    else:
        raise PermissionDenied

def delete_gates(user):
    if user.has_perm('locations.delete_gate'):
        return True
    else:
        raise PermissionDenied

################################################################################################################################################################################
################################################################################# Stands #######################################################################################
################################################################################################################################################################################

def view_stands(user):
    if user.has_perm('locations.view_stand'):
        return True
    else:
        raise PermissionDenied

def add_stands(user):
    if user.has_perm('locations.add_stand'):
        return True
    else:
        raise PermissionDenied

def update_stands(user):
    if user.has_perm('locations.change_stand'):
        return True
    else:
        raise PermissionDenied

def delete_stands(user):
    if user.has_perm('locations.delete_stand'):
        return True
    else:
        raise PermissionDenied

################################################################################################################################################################################
################################################################################# PBBs #########################################################################################
################################################################################################################################################################################

def view_pbbs(user):
    if user.has_perm('locations.view_pbb'):
        return True
    else:
        raise PermissionDenied

def add_pbbs(user):
    if user.has_perm('locations.add_pbb'):
        return True
    else:
        raise PermissionDenied

def update_pbbs(user):
    if user.has_perm('locations.change_pbb'):
        return True
    else:
        raise PermissionDenied

def delete_pbbs(user):
    if user.has_perm('locations.delete_pbb'):
        return True
    else:
        raise PermissionDenied