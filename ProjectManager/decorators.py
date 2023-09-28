#from django.utils import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def admin(user):
    if user.groups.filter(name='Admin').exists():
        return user.groups.filter(name='Admin').exists()
    else:
        raise PermissionDenied

def editor(user):
    if user.groups.filter(name='Editor').exists():
        return user.groups.filter(name='Editor').exists()
    else:
        raise PermissionDenied

def creator(user):
    if user.groups.filter(name='Creator').exists():
        return user.groups.filter(name='Creator').exists()
    else:
        raise PermissionDenied

def viewer(user):
    if user.groups.filter(name='Viewer').exists():
        return user.groups.filter(name='Viewer').exists()
    else:
        raise PermissionDenied

def operator(user):
    if user.groups.filter(name='Operator').exists():
        return user.groups.filter(name='Operator').exists()
    else:
        raise PermissionDenied



#def group_required(group, login_url=None, raise_exception=False):
#    """
#    Decorator for views that checks whether a user has a group permission,
#    redirecting to the log-in page if necessary.
#    If the raise_exception parameter is given the PermissionDenied exception
#    is raised.
#    """
#    def check_perms(user):
#        if isinstance(group, six.string_types):
#            groups = (group, )
#        else:
#            groups = group
#        # First check if the user has the permission (even anon users)
#
#        if user.groups.filter(name__in=groups).exists():
#            return True
#        # In case the 403 handler should be called raise the exception
#        if raise_exception:
#            raise PermissionDenied
#        # As the last resort, show the login form
#        return False
#    return user_passes_test(check_perms, login_url=login_url)