from dataclasses import field
import django_filters

from accounts.models import CustomUser
from django.contrib.auth.models import Group
from locations.models import Terminal

class UserFilter(django_filters.FilterSet):
    groups     = django_filters.ModelChoiceFilter(field_name='groups', queryset=Group.objects.all())
    location   = django_filters.ModelChoiceFilter(field_name='location', queryset=Terminal.objects.all())

    class Meta:
        model = CustomUser
        fields = ['groups', 'location']

def filter_accounts(search, field):
    filtered_records = CustomUser.objects.none()

    if field == "username":
        filtered_records = CustomUser.objects.filter(is_superuser = False, username__icontains  = search).order_by('groups')
    elif field == "first_name":
        filtered_records = CustomUser.objects.filter(is_superuser = False, first_name__icontains  = search).order_by('groups')
    elif field == "last_name":
        filtered_records = CustomUser.objects.filter(is_superuser = False, last_name__icontains  = search).order_by('groups')
    elif field == "user_id":
        filtered_records = CustomUser.objects.filter(is_superuser = False, user_id__icontains  = search).order_by('groups')
    elif field == "email":
        filtered_records = CustomUser.objects.filter(is_superuser = False, email__icontains = search).order_by('groups')
    
    return filtered_records