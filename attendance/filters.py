import django_filters
from accounts.models import CustomUser
from django.contrib.auth.models import Group
from .models import Shift
from django.db.models import Q

class ShiftFilter(django_filters.FilterSet):
    name     = django_filters.ModelMultipleChoiceFilter(field_name='name', lookup_expr='icontains', queryset=Shift.objects.all())

    class Meta:
        model = Shift
        fields = ['name',]

def filter_accounts(search, field):
    filtered_records = CustomUser.objects.none()

    if field == "name":
        filtered_records = CustomUser.objects.filter(
                Q(is_superuser = False) &
                Q(
                    Q(username__icontains  = search) |
                    Q(first_name__icontains  = search) |
                    Q(last_name__icontains  = search)
                )
            ).order_by('groups')
    
    return filtered_records